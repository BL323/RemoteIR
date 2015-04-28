from app import db

class Task(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	action = db.Column(db.String(64), index=True)
	time = db.Column(db.DateTime, index=True)
	hasRan = db.Column(db.Boolean, index=True)

	def __repr__(self):
		return '<Task: %r @ %r>' % (self.action, self.time)
