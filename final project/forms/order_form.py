from flask_wtf import FlaskForm
from wtforms import SubmitField

# форма для оформления заказа
class OrderForm(FlaskForm):
    submit = SubmitField('Применить')