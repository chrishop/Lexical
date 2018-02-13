#!/usr/local/bin/python3

import subprocess,os
cwd = str(os.getcwd()) + '/Project/run.py'
subprocess.call(['python3',cwd])