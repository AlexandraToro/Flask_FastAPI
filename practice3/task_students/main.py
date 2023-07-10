import random
from flask import Flask, render_template
from task_students.models import db, Student, Faculty, Mark

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)
gender = ['male', 'female']


@app.route('/')
def index():
	return "hello"


@app.cli.command('init-db')
def init_db():
	db.create_all()
	print('OK')


@app.cli.command("fill-data")
def add_test_data():
	count = 5
	for i in range(1, count + 1):
		faculty = Faculty(name=f"faculty{i}")
		db.session.add(faculty)
		for j in range(1, 3):
			student = Student(
				name=f"name{i}{j}",
				lastname=f"surname{i}{j}",
				age=random.randint(18, 25),
				group=2,
				gender=random.choice(gender),
				email=f"student{i}{j}@mail.ru",
				faculty_id=i
			)
			db.session.add(student)
	for k in range(1, 11):
		mark = Mark(name='biology',
		            mark=random.randint(2, 6),
		            student_id=k
		            )
		db.session.add(mark)
	
	db.session.commit()
	print('данные добавлены')


@app.route('/students/')
def all_students():
	students = Student.query.all()
	context = {'students': students}
	return render_template('students.html', **context)


if __name__ == "__main__":
	app.run(debug=True)
