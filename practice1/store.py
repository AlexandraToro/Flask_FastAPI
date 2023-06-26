from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def master():
	return render_template('index.html')

@app.route('/shoes/')
def show_shoes():
	return render_template('shoes.html')

@app.route('/shoes/snicker/')
def show_snicker():
	return render_template('snicker.html')

if __name__ == '__main__':
	app.run()
