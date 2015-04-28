from app import db, models
import datetime

def GetAllTasks():
	tasks = models.Task.query.all()
	return tasks

def AddTask():
	return "d"

def DeleteTask():
	return "t"
