from flask_wtf import FlaskForm
from wtforms import SubmitField

# форма для добавления товара в корзину
class To_korzina(FlaskForm):
    submit = SubmitField('В корзину')