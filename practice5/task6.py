# Задание №6
# * Создать веб-страницу для отображения списка пользователей. Приложение
# должно использовать шаблонизатор Jinja для динамического формирования HTML
# страницы.
# * Создайте модуль приложения и настройте сервер и маршрутизацию.
# * Создайте класс User с полями id, name, email и password.
# * Создайте список users для хранения пользователей.
# * Создайте HTML шаблон для отображения списка пользователей. Шаблон должен
# содержать заголовок страницы, таблицу со списком пользователей и кнопку для
# добавления нового пользователя.
# * Создайте маршрут для отображения списка пользователей (метод GET).
# * Реализуйте вывод списка пользователей через шаблонизатор Jinja.


from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, EmailStr, Field

app = FastAPI()
templates = Jinja2Templates(directory="templates")


class User(BaseModel):
	id: int
	name: str
	email: EmailStr
	password: str


class UserUpdate(BaseModel):
	name: str
	email: EmailStr = Field(..., description="Email of user")
	password: str = Field(..., min_length=8, description="Password of user")


users = [User(id=i, name=f"name_{i}", email=f"mail{i}@gmail.com", password=f"{i}") for i in range(1, 6)]


@app.get("/users", response_class=HTMLResponse, response_model=list[User], summary="Show all user", tags=["Users"])
async def read_users(request:Request):
	return templates.TemplateResponse("user.html", {"request":request, "users":users, "title": "Users"})

