#!flask/bin/python
from app import app
from Scheduler import Scheduler
import threading
from flask.ext.login import LoginManager, UserMixin, login_required, current_user

t = threading.Thread(target=Scheduler.start)
t.start()
print "Started polling"
app.run(debug = True, host="0.0.0.0")


print "Started server"

@app.teardown_appcontext
def shutdown_session(exception=None):
	app.db_session.remove()



