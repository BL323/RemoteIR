from flask.ext.wtf import Form
from wtforms import StringField, DateTimeField, SelectField, IntegerField
from wtforms.validators import DataRequired

class AddTaskForm(Form):
	action = SelectField(u'Action', choices=[('ON', 'ON'), ('OFF', 'OFF')])
	hour = StringField(u'Hour')