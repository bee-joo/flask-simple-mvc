from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, NumberRange

class Form(FlaskForm):

    first_name = StringField("Имя: ", validators=[DataRequired()])
    last_name = StringField("Фамилия: ", validators=[DataRequired()])
    email = StringField("Email: ", validators=[Email()])
    city = StringField("Город: ", validators=[DataRequired()])
    post_index = IntegerField("Индекс: ", validators=[DataRequired(), NumberRange(min = 100000, max = 999999)])
    address = StringField("Адрес: ", validators=[DataRequired()])
    submit = SubmitField("Отправить")