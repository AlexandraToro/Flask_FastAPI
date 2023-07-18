from fastapi import APIRouter
from db import products, database
from models import Product, ProductIn

router = APIRouter()

@router.get("/goods/{amt}")
async def create_goods(amt: int):
	for i in range(1, amt + 1):
		query = products.insert().values(name=f'a_good{i}',
		                               description=f'=={i ** 4}=='
		                                           f'Lorem  ipsum  dolor  sit amet, '
		                                           f'consectetur  adipiscing  elit. '
		                                           f'Vestibulum    sagittis   dolor '
		                                           f'mauris,  at  elementum  ligula '
		                                           f'tempor  eget.'
		                                           f'=={i ** 4}==',
		                               price=round(i ** 2 / (i * 2) + i ** 2 / i ** 3, 2),
		                               )
		await database.execute(query)
	return {'message': f'{amt} fake goods created'}


@router.post("/products/", response_model=Product)
async def create_product(product: ProductIn):
	query = products.insert().values(**product.model_dump())
	last_record_id = await database.execute(query=query)
	return Product(**product.model_dump(), id=last_record_id)


@router.get("/products/", response_model=list[Product])
async def get_all():
	query = products.select()
	return await database.fetch_all(query=query)


@router.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: int):
	query = products.select().where(products.c.id == product_id)
	return await database.fetch_one(query)


@router.put("products/update/{product_id}", response_model=Product)
async def update_products(product_id: int, new_data: ProductIn):
	query = products.update().where(products.c.id == product_id).values(**new_data.model_dump())
	await database.execute(query)
	return {**new_data.model_dump(), "id": product_id}


@router.delete("products/delete")
async def delete_product(product_id: int):
	query = products.delete().where(products.c.id == product_id)
	await database.execute(query)
	return {'message': 'Success! Product deleted.'}
