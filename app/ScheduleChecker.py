from app import db, models
from flask import flash
import datetime
import time


def GetDateTimes():
	currTime = datetime.datetime.now()
	print "performing Query"

	task = models.Task.query.filter_by(id=3).first()
	print "printing tasks"
	print tasks


def LoopChecker():
	flash("starting loop")
	while True:
		GetDateTimes()
		time.sleep(5)
