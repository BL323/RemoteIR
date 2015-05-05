from flask import render_template, redirect, flash, request, Response
import datetime
from app import app, db, models, logger
from PiController import *
from RemoteDAL import *
from .forms import AddTaskForm
from .auth import User
from flask.ext.login import login_required, login_user, logout_user, current_user
import Cookie

@app.route('/')
@app.route('/index')
def index():
	form = AddTaskForm()
	return render_template("index.html", tasks=GetAllTasks(), form=form)

#@login_required
#@app.route('/test')
#def protected():
#	if current_user.is_authenticated():
#  		return Response(response="Hello Auth World!", status=200)
#  	else:
# 		return Response(response="Non_Auth World!", status=200)


#@login_required
#@app.route('/temp')
#def logout():
	#logout_user()
#	return redirect("/index", code=302) 

@app.route('/On')
def immediateActionOn():
	PiOn()
	logger.error('Immediate Turn On')
	return redirect("/index",code=302)

@app.route('/Off')
def immediateActionOff():
	PiOff()
	logger.error('Immediate Turn Off')
	return redirect("/index", code=302)

@app.route('/AddTask', methods=['GET', 'POST'])
def addTaskToDB():
	form = AddTaskForm()

	if form.validate_on_submit():
		dt = GetDateTime(request.form['date'], form.hour.data)

		if dt is None:
			return render_template("error.html")
		else:			
			t = models.Task(action=form.action.data, time=dt,hasRan=False)
			AddTask(t)
			return redirect("/index", code=302)
	else:
		return render_template("error.hmtl")

@app.route('/RemoveTask')
def removeTaskFromDB():
	taskId = request.args.get('tid')
	DeleteTask(taskId)
	return redirect("/index", code=302)

#@app.route('/login', methods=['Get', 'Post'])
#def displayLogin():

#	if len(request.form) > 0:
#		usr = str(request.form['user_name'])
#		pwd =  str(request.form['password'])
#		if usr == "ilourence" and pwd == "football":
#			c=Cookie.SimpleCookie()
			# assign a value
#			c['raspberrypi']='Hello world'
			# set the xpires time
#			c['raspberrypi']['expires']=1*1*3*60*60
			

#			return redirect("/index",code=302)
#	return render_template("login.html")





