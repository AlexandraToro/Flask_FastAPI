from databases import Database
from sqlalchemy import MetaData, Column, Integer, String, Table, create_engine, Text, Date, Boolean, ForeignKey
from settings import settings

database = Database(settings.DATABASE_URL)
metadata = MetaData()
users = Table(
	"users",
	metadata,
	Column("id", Integer, primary_key=True),
	Column("first_name", String(settings.MAX_LENGTH_NAME), nullable=True),
	Column("last_name", String(settings.MAX_LENGTH_SURNAME), nullable=True),
	Column("email", String(settings.MAX_LENGTH_SURNAME), nullable=True),
	Column("password", String(settings.MAX_LENGTH_PASSWORD), nullable=True)
)

products = Table(
	"products",
	metadata,
	Column("id", Integer, primary_key=True),
	Column("name", String(200),nullable=True),
	Column("description", Text),
	Column("price", Integer,nullable=True)
)

orders = Table(
	"orders",
	metadata,
	Column("id", Integer, primary_key=True),
	Column("user_id", Integer, ForeignKey('users.id')),
	Column("product_id", Integer, ForeignKey('products.id')),
	Column("date", Date()),
	Column("status", Boolean),
)

engine = create_engine(
	settings.DATABASE_URL, connect_args={"check_same_thread": False}
)

metadata.create_all(engine)

#
# from databases import Database
# from sqlalchemy import MetaData, Column, Integer, String, Table, Date, Float, create_engine, ForeignKey
#
# from settings import settings
#
# db = Database(settings.DATABASE_URL)
#
# metadata = MetaData()
#
# engine = create_engine(
#     settings.DATABASE_URL,
#     connect_args={"check_same_thread": False}
# )
#
# goods = Table(
#     "goods",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("name", String, nullable=False),
#     Column("description", String, nullable=False),
#     Column("price", Float, nullable=False),
# )
#
# customers = Table(
#     "customers",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("name", String(50), nullable=False),
#     Column("surname", String(50), nullable=False),
#     Column("email", String(128), nullable=False),
#     Column("password", String, nullable=False),
# )
#
# orders = Table(
#     "orders",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("customer_id", Integer, ForeignKey('goods.id'), nullable=False),
#     Column("good_id", Integer, ForeignKey('goods.id'), nullable=False),
#     Column("order_date", Date, nullable=False),
#     Column("status", String, nullable=False),
# )
#
# metadata.create_all(engine)
