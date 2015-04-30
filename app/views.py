from flask import render_template, redirect, flash
import datetime
from app import app, db, models
from PiController import *
from RemoteDAL import *
from .forms import AddTaskForm

@app.route('/')
@app.route('/index')
def index():
	form = AddTaskForm()
	return render_template("index.html", tasks=GetAllTasks(), form=form)

@app.route('/On')
def immediateActionOn():
	PiOn()
	return redirect("/index",code=302)

@app.route('/Off')
def immediateActionOff():
	PiOff()
	return redirect("/index", code=302)

@app.route('/AddTask', methods=['GET', 'POST'])
def addTaskToDB():
	form = AddTaskForm()
	if form.validate_on_submit():
		print form.action.data
		t = models.Task(action='ON', time=datetime.datetime.now(),hasRan=False)
		AddTask(t)

	return redirect("/index", code=302)

@app.route('/RemoveTask')
def removeTaskFromDB():
	
	return redirect("/index", code=302)