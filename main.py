
import sys
import os
import fs
import settings
import argparse
import commands

s = settings.settings("settings")

if s.get("installed") != "True":
	print("detecting first run. ")
	import install

#add subparser for every file in commands
#__args__ method is called to retrieve args for that option
#__exec__ method is called to execute option
parser = argparse.ArgumentParser(description='Welcome to V! A versioning system written in python')
options = [i[:-3] for i in os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),"commands")) if i.endswith(".py") and "__" not in i]
subparsers = parser.add_subparsers(help='...')
for i in options:
	s = subparsers.add_parser(i)
	s.set_defaults(option=i)
	try:
		getattr(commands,i).__args__(s)
	except AttributeError:
		print("warning: could not find __args__ method in command {}.".format(i))
		pass
args = parser.parse_args()
try:
	getattr(commands,args.option).__exec__(args)
except AttributeError:
	print("warning: could not find __exec__ method in command {}.".format(args.option))
