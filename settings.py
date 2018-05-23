import os


class settings:
	def __init__(self,file, create=True):
		self.file = file
		self.create = create

	def create(self):
		open(self.file,"w")

	def getall(self):
		try:
			settings = open(self.file).readlines()
		except FileNotFoundError:
			if not self.create:
				return
			self.create()
			settings = open(self.file).readlines()
		return {key:value for key,value in (i.split() for i in settings if i.strip() != "")}

	def get(self,setting):
		try:
			settings = open(self.file).readlines()
		except FileNotFoundError:
			if not self.create:
				return
			self.create()
			settings = open(self.file).readlines()

		for key,value in (i.split() for i in settings if i.strip() != ""):
			if key == setting:
				return value
		return None

	def exists(self,setting):
		return self.get(setting) != None

	def write(self,setting,val):
		try:
			settings = open(self.file).readlines()
		except FileNotFoundError:
			settings = []

		for index,key,value in ([index,*i.split()] for index,i in enumerate(settings) if i.strip() != ""):
			if key == setting:
				settings[index] = "{} {}".format(setting,val)
				break
		else:
			settings.append("{} {}".format(setting,val))
		file = open(self.file,"w")
		for i in settings:
			file.write(i.strip())
			file.write("\n")

	def remove(self):
		os.remove(self.file)