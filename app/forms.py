from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class InputForm(FlaskForm):
    data = StringField('INPUT', validators=[DataRequired()])
