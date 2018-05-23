import settings
import pip

print("installing V.")
pip.main(['install','-r', 'requirements.txt'])

print("V succesfully installed")
settings.write("installed","True")
