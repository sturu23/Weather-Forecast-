from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField


class SearchCity(FlaskForm):
    city = StringField('City')
    submit = SubmitField('Search')