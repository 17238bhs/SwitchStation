from flask_wtf import FlaskForm
from wtforms import IntegerField, TextField, TextAreaField, SelectField, FloatField
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
    cost = FloatField('cost', validators=[DataRequired()])
    actuation = FloatField('actuation', validators=[Optional()])
    bottomout = FloatField('bottomout', validators=[Optional()])
    pretravel = FloatField('pretravel', validators=[Optional()])
    totaltravel = FloatField('totaltravel', validators=[Optional()])

class Edit_Switch(FlaskForm): # Edit switch form
    name = TextField('name', validators=[DataRequired()])
    manufacturer = TextField('manufacturer', validators=[DataRequired()])
    style = TextField('style', validators=[DataRequired()])
    color = TextField('color', validators=[DataRequired()])
    description = TextAreaField('description', validators=[Optional()])
    cost = FloatField('cost', validators=[DataRequired()])
    actuation = FloatField('actuation', validators=[Optional()])
    bottomout = FloatField('bottomout', validators=[Optional()])
    pretravel = FloatField('pretravel', validators=[Optional()])
    totaltravel = FloatField('totaltravel', validators=[Optional()])