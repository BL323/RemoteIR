from app import db, models
import datetime

def GetAllTasks():
	tasks = models.Task.query.all()
	return tasks

def AddTask(t):
	db.session.add(t)
	db.session.commit()

def DeleteTask():
	return "t"
