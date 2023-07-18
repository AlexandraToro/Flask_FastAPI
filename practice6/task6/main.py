import uvicorn
from fastapi import FastAPI
from db import database
import user_router, product_router, order_router

app = FastAPI(title="lesson-6")

app.include_router(user_router.router, tags=["USER"])
app.include_router(product_router.router, tags=["PRODUCT"])
app.include_router(order_router.router, tags=["ORDER"])


@app.on_event("startup")
async def startup():
	await database.connect()


@app.on_event("shutdown")
async def shutdown():
	await database.disconnect()


if __name__ == '__main__':
	uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


