from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Email, Length, EqualTo, InputRequired, ValidationError


class RegistrationForm(FlaskForm):
	name = StringField('Имя', validators=[InputRequired()])
	surname = StringField('Фамилия', validators=[InputRequired()])
	email = StringField('Email', validators=[InputRequired(), Email()])
	password = PasswordField('Пароль', validators=[InputRequired(), Length(min=8)])
	confirm_password = PasswordField('Подтверждение пароля', validators=[InputRequired(),
	                                                                     EqualTo('password')])
	personal_data = BooleanField(label=('Согласен(на) на обработку персональных данных'), name=None)
	submit = SubmitField('Зарегистрироваться')
	

	

