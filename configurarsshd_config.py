#! /usr/bin/python

import os
import time


def sshd_config():
	
	archivo = open ('/etc/ssh/sshd_config','r')
	lines = list(archivo)
	archivo.close()

	archivo = open ('sshd_config','w')
	for i in range(len(lines)):
		if 'PermitRootLogin' in lines[i]:
			lines[i] = 'PermitRootLogin yes\n'
		archivo.write (lines[i])
	archivo.close()
	try:

		os.system("mv sshd_config /etc/ssh/")
	except:
		print("Error mover sshd_condif")
		return 0
	return 1
		


if(sshd_config() != 0):
	print ("CORRECTO---> Configuracion de SSHD_CONFGI ")
	time.sleep(2)
else:
	print("Error en: Funcion -->sshd_config")


#C:\Users\fdg\Documents\Python\Finalizando\asd
#dire = "C:\Users\\fdg\Documents\Python\Finalizando\\asd"
#dire2= "C:\ "
#sshd_config()
#system ('mv sshd_config /etc/ssh/')
#chdir(dire)
#system ('move asd C:\ ')
#print ("\\f")