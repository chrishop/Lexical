import os
os.system("cd Project")
cwd = str(os.getcwd()) + "\Project"
os.chdir(cwd)
os.system("python run.py")
