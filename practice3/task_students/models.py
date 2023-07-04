from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(60), nullable=False)
	lastname = db.Column(db.String(60), nullable=False)
	age = db.Column(db.Integer, nullable=False)
	group = db.Column(db.Integer)
	gender = db.Column(db.String(20), nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'), nullable=False)
	marks = db.relationship('Mark', backref='Student', lazy=True)
	
	def __repr__(self):
		return f'Student ({self.name}, {self.lastname}, {self.faculty_id})'


class Faculty(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(60), nullable=False)
	students = db.relationship('Student', backref='Faculty', lazy=True)
	
	def __repr__(self):
		return f'Faculty ({self.name}'


class Mark(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
	name = db.Column(db.String(60), nullable=False)
	mark = db.Column(db.Integer, nullable=False)
	
	def __repr__(self):
		return f'Mark ({self.name}, {self.mark}'
	
