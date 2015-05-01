from app import db, models
import datetime

def GetAllTasks():
	tasks = models.Task.query.all()
	return tasks

def AddTask(t):
	db.session.add(t)
	db.session.commit()

def DeleteTask(taskId):
	task = models.Task.query.filter_by(id=taskId).first()
	
	db.session.delete(task)
	db.session.commit()

def GetDateTime(dateStr, timeStr):
	monthNumDict = {
		'January' : 1,
        'February' : 2,
        'March' : 3,
        'April' : 4,
        'May' : 5,
        'June' : 6,
        'July' : 7,
        'August' : 8,
        'September' : 9, 
        'October' : 10,
        'November' : 11,
        'December' : 12
        }

	t = dateStr.split(',')
	year = t[1]
	k = t[0].split(' ')
	day = k[0]
	monthName = k[1]
	monthNum = monthNumDict[monthName]

	h = timeStr.split(':')
	hours = h[0]
	mintues = h[1]

	dt = datetime.datetime(int(year), int(monthNum), int(day), int(hours),int(mintues))
	return dt