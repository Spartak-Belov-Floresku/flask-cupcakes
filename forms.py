from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField
from wtforms.validators import InputRequired, Optional, NumberRange, URL

class CupcakeForm(FlaskForm):
    """generate form to add pet into db"""
    rate = [(i, f'Rating {i}') for i in range(1,11)]
    flavor = StringField('Flavor', validators=[InputRequired()])
    size = SelectField('Size', choices=[('large', 'Large'), ('medium', 'Medium'), ('small', 'Small')])
    rating = SelectField('Rating', choices=rate)
    image = StringField('URL image', validators=[Optional(), URL()])