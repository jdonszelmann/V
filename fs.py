import os
from os import path
import shutil
from security import authorize
import tarfile
import time
import datetime
import settings

RunningDir = path.dirname(path.abspath(__file__))
CurrentDir = os.getcwd


def is_V_dir(location):
	try:
		return os.path.isfile(path.join(CurrentDir(),location,".Version","V")) 
	except FileNotFoundError:
		return False
	except PermissionError:
		return False

def setup_V_dir(location):
	if is_V_dir(location):
		print("V directory already initialized.")
		return
	try:
		os.mkdir(path.join(CurrentDir(),location,".Version"))
		Vsettings = settings.settings(path.join(CurrentDir(),location,".Version","V"),create=True)
		Vsettings.write("Vdir","True")
		Vsettings.write("commits","0") 
	except FileExistsError:
		print("V directory already initialized.")
	except FileNotFoundError:
		print("could not find folder.")
	except PermissionError:
		print("could not initialize due to inadequate permissions. (Suggested solution: use Sudo")

@authorize
def remove_V_dir(location):
	try:
		if is_V_dir(location):
			shutil.rmtree(path.join(CurrentDir(),location,".Version"))
		else:
			print("not a V directory.")
	except FileNotFoundError:
		print("could not find folder.")
	except PermissionError:
		print("could not initialize due to inadequate permissions. (Suggested solution: use Sudo")

def commit(message):
	if not is_V_dir("."):
		print("initialize V first (V init)")
		return

	s = settings.settings(path.join(CurrentDir(),".__data__"),create=True)
	s.write("message",repr(message))
	s.remove()
	name = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S')
	with tarfile.open('{}.tar.gz'.format(path.join(CurrentDir(),".Version",name)), mode='w:gz') as archive:
		archive.add(path.join(CurrentDir()), recursive=True)

	return name
