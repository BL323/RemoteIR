from flask.ext.wtf import Form
from wtforms import StringField, DateTimeField
from wtforms.validators import DataRequired

class AddTaskForm(Form):
	action = StringField('action', validators=[DataRequired()])
	dateTime = DateTimeField('DateTime', validators=[DataRequired()])