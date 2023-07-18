import hashlib
from fastapi import APIRouter
from db import users, database
from models import User, UserIn, UserUpdate

router = APIRouter()

# create testing data
# @router.get("/users/{count}")
# async def create_testing_data_user(count: int):
# 	for i in range(1, count + 1):
# 		query = users.insert().values(
# 			first_name=f'Username_{i}',
# 			last_name=f'Usersurname_{i}',
# 			email=f'{i}@mail.com',
# 			password=f'password{i **2/i*2, 3}',
# 		)
# 		await database.execute(query)
# 	return {'message': f'Testing data done'}


@router.post("/users/", response_model=User)
async def create_user(user: UserIn):
	password_hash = hashlib.sha1(b'user.password').hexdigest()
	user.password = password_hash
	query = users.insert().values(**user.model_dump())
	last_record_id = await database.execute(query=query)
	return User(**user.model_dump(), id=last_record_id)


@router.get("/users/", response_model=list[User])
async def get_all():
	query = users.select()
	return await database.fetch_all(query=query)


@router.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
	query = users.select().where(users.c.id == user_id)
	return await database.fetch_one(query)


@router.put("users/update/{user_id}", response_model=User)
async def update_user(user_id: int, new_data: UserUpdate):
	query = users.update().where(users.c.id == user_id).values(**new_data.model_dump())
	await database.execute(query)
	return {**new_data.model_dump(), "id": user_id}


@router.delete("users/delete")
async def delete_user(user_id: int):
	query = users.delete().where(users.c.id == user_id)
	await database.execute(query)
	return {'message': 'Success! User deleted.'}
