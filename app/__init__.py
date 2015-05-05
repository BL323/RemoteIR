from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import logging

app = Flask(__name__)
app.config.from_object("config")
db = SQLAlchemy(app)

logger = logging.getLogger('myapp')
hdlr = logging.FileHandler('/var/tmp/RemoteIR.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.WARNING)
#login_manager.init_app(app)

from app import views, models

