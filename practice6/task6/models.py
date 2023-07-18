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

# owner = relationship("User", back_populates="orders")
# product = relationship("Product", back_populates="orders")

##
# class User(BaseModel):
# 	__tablename__ = "users"
#
# 	id = d.Column(Integer, primary_key=True)
# 	first_name = d.Column(String, nullable=True)
# 	last_name = d.Column(String, nullable=True)
# 	email = d.Column(String, unique=True, nullable=True)
# 	password = d.Column(String)
#
# 	orders = relationship("Orders", backref='User', lazy=True)
#
# 	def __repr__(self):
# 		return f" User {self.first_name}"
#
#
# class Products(BaseModel):
# 	__tablename__ = "products"
#
# 	id = d.Column(Integer, primary_key=True, index=True)
# 	name = d.Column(String, index=True)
# 	description = d.Column(String, index=True)
# 	price = d.Column(DECIMAL)
#
# 	orders = relationship("Orders", backref="Product", lazy=True)
#
# 	def __repr__(self):
# 		return f" Product {self.name}"
#
#
# class Orders(BaseModel):
# 	__tablename__ = "orders"
# 	id = d.Column(Integer, primary_key=True),
# 	user_id = d.Column(Integer, ForeignKey("users.id")),
# 	product_id = d.Column(Integer, ForeignKey("products.id")),
# 	date = d.Column(Date()),
# 	status = d.Column(Boolean),
