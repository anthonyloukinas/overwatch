from flask import render_template
#Import variables stored in _init_.py
from app import app

@app.route('/')
def index():
 import subprocess
 cmd = subprocess.Popen(['ps', 'aux'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 stdout,error = cmd.communicate()
 memory = stdout.splitlines()
 
 cmd1 = subprocess.Popen(['uptime'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 stdout1,error1 = cmd1.communicate()
 uptime = stdout1.splitlines()
   
 return render_template('index.html', memory=memory, uptime=uptime) 
 
