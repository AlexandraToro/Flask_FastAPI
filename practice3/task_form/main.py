from flask import Flask, request, render_template
from flask_wtf.csrf import CSRFProtect
import hashlib

from task_form.forms import RegistrationForm
from task_form.models import db, User

# Задание
# Создать форму для регистрации пользователей на сайте.
# Форма должна содержать поля "Имя", "Фамилия", "Email", "Пароль" и кнопку "Зарегистрироваться".
# При отправке формы данные должны сохраняться в базе данных, а пароль должен быть зашифрован.

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///users.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
	db.create_all()


@app.route('/register/', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if request.method == 'POST' and form.validate():
		name = form.name.data
		surname = form.surname.data
		email = form.email.data
		password = hashlib.sha1(b'form.password.data').hexdigest()
		existing_email = User.query.filter((User.email == email)).first()
		if existing_email:
			error_msg = 'E-mail already exists.'
			form.email.errors.append(error_msg)
			return render_template('register.html', form=form)
		new_user = User(name=name, surname=surname, email=email, password=password)
		db.session.add(new_user)
		db.session.commit()
		msg = 'Регистрация прошла успешно!'
		return msg
	return render_template('register.html', form=form)
