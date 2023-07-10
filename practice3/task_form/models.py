from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(60), nullable=False)
	surname = db.Column(db.String(60), nullable=False)
	email = db.Column(db.String(120), nullable=False, unique=True)
	password = db.Column(db.String(60), nullable=False)

	