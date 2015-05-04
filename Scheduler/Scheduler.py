import os
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '../app.db')

print SQLALCHEMY_DATABASE_URI

class Task(declarative_base()):
	__tablename__ = "task"
	id = Column(Integer, primary_key=True)
	action = Column(String)
	time = Column(DateTime)
	hasRan = Column(Boolean)

	def __repr__(self):
		return '<Task: %r @ %r>' % (self.action, self.time)

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
t = session.query(Task).filter_by(hasRan=False).first() 
print t
