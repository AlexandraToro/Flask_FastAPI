from datetime import datetime
from pydantic import BaseModel, Field, EmailStr
from settings import settings
from decimal import Decimal


class UserIn(BaseModel):
	first_name: str = Field(..., min_length=2, max_length=settings.MAX_LENGTH_NAME)
	last_name: str = Field(..., min_length=2, max_length=settings.MAX_LENGTH_SURNAME)
	email: EmailStr = Field(..., unique=True)
	password: str = Field(..., max_length=128, min_length=8)


class UserUpdate(BaseModel):
	first_name: str = Field(..., min_length=2, max_length=settings.MAX_LENGTH_NAME)
	last_name: str = Field(..., min_length=2, max_length=settings.MAX_LENGTH_SURNAME)
	email: EmailStr = Field(..., unique=True)


class User(UserUpdate):
	id: int


class ProductIn(BaseModel):
	name: str = Field(..., max_length=200)
	description: str = Field(..., max_length=1000)
	price: Decimal


class Product(ProductIn):
	id: int


class OrderIn(BaseModel):
	user_id: int
	product_id: int
	date: datetime
	status: bool


class Order(OrderIn):
	id: int
