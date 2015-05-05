# flask_tracking/auth.py
from flask.ext.login import LoginManager, UserMixin, login_user


#login_manager = LoginManager()
#login_manager.login_view = "login"
# We have not created the users.login view yet
# but that is the name that we will use for our
# login view, so we will set it now.

class User(UserMixin):
    # proxy for a database of users
    user_database = {"ilourence": ("ilourence", "football")}
 
    def __init__(self, username, password):
        self.id = username
        self.password = password
 
    @classmethod
    def get(cls,id):
        return cls.user_database.get(id)

#@login_manager.user_loader
#def load_user(id):
	#print "LOAD USER"
	#token = request.headers.get('Authorization')
	#if token is None:
	#	print "Token is None"
    # 	token = request.args.get('token')
    #  	print token

 	#if token is not None:
 	#	print "token is not None"
 	#	username,password = token.split(":") #
 	#login_user(User("ilourence", "football"))

#	return User.get("ilourence")


#@login_manager.request_loader
#def load_user(request):

	#u = User("ilourence", "football")
	#return u
#	token = request.headers.get('Authorization')
	#print token
	#if token is None:
#		token = request.args.get('token')

#	if token is not None:

#		return User("ilourence", "football")
        

#  	return None