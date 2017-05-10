
import subprocess

proc = subprocess.Popen(['python', 'subprocesos1.py'],  stdin=subprocess.PIPE)
proc.communicate('\n Hello?\n')
#Received: Hello?(None, None)
