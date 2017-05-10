#import pexpect
import sys
from pexpect import pxssh 
import getpass

user = 'root'
try:
	host = '192.168.179.139'
except IndexError:
	print ("Must have host name or ip address")
	sys.exit(1)

password = '123456'
try:
	s = pxssh.pxssh()
	s.force_password = True
	s.login (host, user, password, login_timeout=20)
	s.sendline ('ls -l') # run a command
	s.prompt() # match the prompt
	print s.before,s.after
	s.interact()
except pxssh.ExceptionPxssh, e:
	print ("pxssh failed on login.")
	print str(e)
	#except OSError:

print ("End session to " + user +"@" + host)