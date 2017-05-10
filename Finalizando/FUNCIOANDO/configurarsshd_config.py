
import os 
import time 

def sshd_config():

	try:
		
		archivo = open ('/etc/ssh/sshd_config','r')
		lines = list(archivo)
		archivo.close()
		
	except:
		print ("Error.Copiado del Archivo ")
		return 0
	try:

		archivo = open ('sshd_config','w')
		for i in range(len(lines)):
			if 'PermitRootLogin' in lines[i]:
				lines[i] = 'PermitRootLogin yes\n'
			archivo.write (lines[i])
		archivo.close()
		
	except:
		print("Error.Modificacion del Archivo ")
		return 0
	try:

		os.system("mv sshd_config /etc/ssh/")
		
	except:
		print ("Error.No se pudo mover sshd_config ")
		return 0

if(sshd_config() != 0):
	print ("CORRECTO---> Configuracion de SSHD_CONFGI ")
	time.sleep(1)
else:
	print("Error en: Funcion -->sshd_config")

os.system("service ssh restart")


