import time
import datetime
import os
from sqlalchemy import Column, Integer, String, Boolean, DateTime, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from threading import Thread
import logging

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '../app.db')

class Task(declarative_base()):
	__tablename__ = "task"
	id = Column(Integer, primary_key=True)
	action = Column(String)
	time = Column(DateTime)
	hasRan = Column(Boolean)

	def __repr__(self):
		return '<Task: %r @ %r>' % (self.action, self.time)

def LoopChecker(Session):
	session = Session()
	
	curTime = datetime.datetime.now()
	tasks = session.query(Task).filter(and_(Task.hasRan == False, Task.time < curTime))

	print "Printing Tasks..."
	for task in tasks:
		print task
		if task.action == "ON":
			print "TURNING ON"
			logger.error('Scheduled Turn On')

		elif task.action == "OFF":
			print "TURNING OFF"
			logger.error('Scheduled Turn Off')


		session.delete(task)
		session.commit()
		session.close()


def start():
	logger = logging.getLogger('myapp')
	hdlr = logging.FileHandler('/var/tmp/RemoteIR.log')
	formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
	hdlr.setFormatter(formatter)
	logger.addHandler(hdlr) 
	logger.setLevel(logging.WARNING)

	engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
	Session = sessionmaker()
	Session.configure(bind=engine)

	#t = session.query(Task).filter_by(hasRan=False).first() 

	while True:
		LoopChecker(Session)
		time.sleep(10)

#import pdb; pdb.set_trace()
