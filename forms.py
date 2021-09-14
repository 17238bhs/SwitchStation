from flask_wtf import FlaskForm
from wtforms import IntegerField, TextField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Optional, ValidationError
import models
from datetime import datetime

class Add_Switch(FlaskForm): # Add a switch form
    # Declaring Fields, validator specifies whether required or optional
    name = TextField('name', validators=[DataRequired()])
    manufacturer = TextField('manufacturer', validators=[DataRequired()])
    style = TextField('style', validators=[DataRequired()])
    color = TextField('color', validators=[DataRequired()])
    description = TextAreaField('description', validators=[Optional()])
    actuation = IntegerField('actuation', validators=[Optional()])
    bottomout = IntegerField('bottomout', validators=[Optional()])
    pretravel = IntegerField('pretravel', validators=[Optional()])
    totaltravel = IntegerField('totaltravel', validators=[Optional()])