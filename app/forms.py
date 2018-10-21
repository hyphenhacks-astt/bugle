from flask_wtf import FlaskForm 
from wtforms import StringField, RadioField
from wtforms.validators import DataRequired

class InputForm(FlaskForm):
    data = StringField('INPUT', validators=[DataRequired()])
    swing = RadioField('SWING', validators=[DataRequired()],choices=(("swing","swing it"),("straight","don't")))
