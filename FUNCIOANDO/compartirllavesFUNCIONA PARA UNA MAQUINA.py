import os
import subprocess

def ssh_key_copy_id():

	os.system("ssh-keygen -P ''")

	direcciones=['192.168.179.139','192.168.179.128']

	for i in range(0,len(direcciones)):
		os.system("ssh-copy-id -i ~/.ssh/id_rsa.pub "+direcciones[i])

ssh_key_copy_id()




#def sub():
#	direcciones=['192.168.179.137'],
#	proc = subprocess.Popen(['ssh-keygen', '-P'," ''"],  stdin=subprocess.PIPE, stdout=subprocess.PIPE)
#	proc.communicate(stdout('\n')



