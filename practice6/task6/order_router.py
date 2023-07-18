from fastapi import APIRouter
from db import orders, database
from models import Order, OrderIn
from typing import List

router = APIRouter()


@router.post("/orders/", response_model=Order)
async def create_order(order: OrderIn):
	query = orders.insert().values(**order.model_dump())
	last_record_id = await database.execute(query=query)
	return Order(**order.model_dump(), id=last_record_id)


@router.get("/orders/", response_model=List[Order])
async def get_all():
	query = orders.select()
	return await database.fetch_all(query=query)


@router.get("/orders/{order_id}", response_model=Order)
async def get_order(order_id: int):
	query = orders.select().where(orders.c.id == order_id)
	return await database.fetch_one(query)


@router.put("orders/update/{order_id}", response_model=Order)
async def update_orders(order_id: int, new_data: OrderIn):
	query = orders.update().where(orders.c.id == order_id).values(**new_data.model_dump())
	await database.execute(query)
	return {**new_data.model_dump(), "id": order_id}


@router.delete("orders/delete")
async def delete_order(order_id: int):
	query = orders.delete().where(orders.c.id == order_id)
	await database.execute(query)
	return {'message': 'Success! Order deleted.'}
