from flask import Flask, render_template, request, url_for, make_response, redirect

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')


# Задание №7
# 📌 Создать страницу, на которой будет форма для ввода числа
# и кнопка "Отправить"
# 📌 При нажатии на кнопку будет произведено
# перенаправление на страницу с результатом, где будет
# выведено введенное число и его квадрат.


@app.route('/square', methods=['POST', 'GET'])
def square():
	if request.method == 'POST':
		num = int(request.form.get('num'))
		return f'Квадрат числа {num} равен {num * num}'
	return render_template('square_num.html')


# Задание №9
# 📌 Создать страницу, на которой будет форма для ввода имени
# и электронной почты
# 📌 При отправке которой будет создан cookie файл с данными
# пользователя
# 📌 Также будет произведено перенаправление на страницу
# приветствия, где будет отображаться имя пользователя.
# 📌 На странице приветствия должна быть кнопка "Выйти"
# 📌 При нажатии на кнопку будет удален cookie файл с данными
# пользователя и произведено перенаправление на страницу
# ввода имени и электронной почты.


@app.route('/cookie_task', methods=['POST', 'GET'])
def cookie_task():
	if request.method == 'POST':
		name = request.form.get('name')
		email = request.form.get('email')
		response = make_response(redirect(url_for('hello')))
		response.set_cookie('username', name)
		response.set_cookie('email', email)
		return response
	else:
		response = make_response(render_template("registry.html"))
		response.delete_cookie('username')
		response.delete_cookie('email')
		return response


@app.route('/hello/', methods=['POST', 'GET'])
def hello():
	name = request.cookies.get('username')
	context = {'name': name}
	return render_template('hello.html', **context)


if __name__ == '__main__':
	app.run(debug=True)
