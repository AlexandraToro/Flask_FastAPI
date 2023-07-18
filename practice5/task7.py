# Создать RESTful API для управления списком задач. Приложение должно
# использовать FastAPI и поддерживать следующие функции:
# ○ Получение списка всех задач.
# ○ Получение информации о задаче по её ID.
# ○ Добавление новой задачи.
# ○ Обновление информации о задаче по её ID.
# ○ Удаление задачи по её ID.
# Каждая задача должна содержать следующие поля: ID (целое число),
# Название (строка), Описание (строка), Статус (строка): "todo", "in progress","done".

import logging

from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


class Task(BaseModel):
	id: int
	title: str
	description: Optional[str] = None
	status: str


class Task_Update(BaseModel):
	title: str
	description: Optional[str] = None
	status: str


tasks = [Task(id=1, title="Title", description=None, status="todo"),
         Task(id=2, title="Title2", description=None, status="in progress")]


@app.get("/", response_model=list[Task])
async def read_tasks():
	logger.info('Отработал GET запрос на все задачи.')
	return tasks


@app.get("/tasks/{task_id}", response_model=Task)
async def read_task(task_id: int, q: str = None):
	logger.info('Отработал GET запрос на одну задачу.')
	task = [task for task in tasks if task.id == task_id]
	if task:
		return task[0]
	raise HTTPException(status_code=404, detail="Task not found")


@app.post("/tasks/")
async def create_task(task: Task_Update):
	logger.info('Отработал POST запрос.')
	new_id = 1
	if tasks:
		new_id = max(tasks, key=lambda x: x.id).id + 1
	if task.status.lower() not in ["todo", "in progress", "done"]:
		raise HTTPException(status_code=422, detail="Incorrect status. U can use only 'tоdo', 'in progress' or 'done'")
	new_task = (Task(id=new_id, title=task.title, description=task.description, status=task.status.lower()))
	tasks.append(new_task)


@app.put("/tasks/{task_id}")
async def update_item(task_id: int, task: Task_Update):
	logger.info(f'Отработал PUT запрос для item id = {task_id}.')
	update_task = [t for t in tasks if t.id == task_id]
	if not update_task:
		raise HTTPException(status_code=404, detail="Task not found")
	if task.status.lower() not in ["todo", "in progress", "done"]:
		raise HTTPException(status_code=422, detail="Incorrect status. U can use only 'tоdo', 'in progress' or 'done'")
	update_task[0].title = task.title
	update_task[0].description = task.description
	update_task[0].status = task.status
	return update_task[0]


@app.delete("/tasks/{task_id}")
async def delete_item(task_id: int):
	logger.info(f'Отработал DELETE запрос для item id =	{task_id}.')
	del_task = [t for t in tasks if t.id == task_id]
	if not del_task:
		raise HTTPException(status_code=404, detail="Task not found")
	tasks.remove(del_task[0])
	return f'task id={task_id} remove'
