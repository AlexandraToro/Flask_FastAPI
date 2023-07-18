import hashlib
from fastapi import APIRouter
from db import users, database
from models import User, UserIn, UserUpdate

router = APIRouter()


@router.get("/customers/{amt}")
async def create_customers(amt: int):
	for i in range(1, amt + 1):
		query = users.insert().values(
			first_name=f'Castor - {i}',
			last_name=f'Doe - {i}',
			email=f'castor{i:0>4}@mail{i % 5}.dom',
			password=f'FakePassword{i ^ 3}',
		)
		await database.execute(query)
	return {'message': f'{amt} fake customers created'}


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

# =================================================
# = Create simple fake customers for initial test =
# =================================================
# @router.get("/customers/{amt}")
# async def create_customers(amt: int):
#     for i in range(1, amt + 1):
#         query = customers.insert().values(
#             name=f'Castor - {i}',
#             surname=f'Doe - {i}',
#             email=f'castor{i:0>4}@mail{i%5}.dom',
#             password=f'FakePassword{i^3}',
#         )
#         await db.execute(query)
#     return {'message': f'{amt} fake customers created'}
# ========================================

#
# @router.post("/customers/", response_model=Customer)
# async def add_customer(customer: CustomerBillet):
#     query = customers.insert().values(**customer.dict())
#     last_id = await db.execute(query)
#     return {**customer.dict(), "id": last_id}
#
#
# @router.get("/customers/", response_model=List[Customer])
# async def read_customers():
#     query = customers.select()
#     return await db.fetch_all(query)
#
#
# @router.get("/customers/{customer_id}", response_model=Customer)
# async def read_customer(customer_id: int):
#     query = customers.select().where(customers.c.id == customer_id)
#     return await db.fetch_one(query)
#
#
# @router.put("/customers/{customer_id}", response_model=Customer)
# async def update_customer(customer_id: int, new_customer: CustomerBillet):
#     query = customers.update().where(customers.c.id == customer_id).values(**new_customer.dict())
#     await db.execute(query)
#     return {**new_customer.dict(), "id": customer_id}
#
#
# @router.delete("/customers/{customer_id}")
# async def delete_customer(customer_id: int):
#     query = customers.delete().where(customers.c.id == customer_id)
#     await db.execute(query)
#     return {"message": "A customer removed from base"}
