import settings
import hashlib, uuid, getpass

s = settings.settings("settings")

def make_account():
	uname = input("username>>>")
	pw = getpass.getpass('Password>>>') 
	autouname = input("do you want to enable automatic usernames? [yes/no]>>>")
	if "y" in autouname:
		print("automatic usernames enables")
		s.write("automatic_uname","True")
	else:
		print("automatic usernames disabled")
		s.write("automatic_uname","False")
	password = hashlib.sha512((pw).encode("utf-8")).hexdigest()

	s.write("username",uname)
	s.write("password",password)

def login(attempts=5):
	return "y" in input("are you sure you want to continue? [yes/no]>>>")
	# if attempts == 0:
	# 	return False
	# if not (s.exists("username") and s.exists("password")):
	# 	print("no account detected. please make one:")
	# 	make_account()

	# if s.get("automatic_uname") == "True":
	# 	uname = s.get("username")
	# else:
	# 	uname = input("username>>>")
	# pw = getpass.getpass('Password>>>') 
	# password = hashlib.sha512((pw).encode("utf-8")).hexdigest()

	# if s.get("username") == uname and s.get("password") == password:
	# 	return True
	# else:
	# 	print("incorrect username or password, please retry. {} attempts left".format(attempts-1))
	# 	login(attempts-1)
		


def authorize(func):
	def retfunc(*args,**kwargs):
		print("this function might cause damage")
		print("please confirm this action")
		if login():
			func(*args,**kwargs)
		else:
			print("confirmation failed")
	return retfunc
