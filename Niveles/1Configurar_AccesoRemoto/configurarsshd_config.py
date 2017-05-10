


def sshd_config():

	try:

		archivo = open ('/etc/ssh/sshd_config','r')
		lines = list(archivo)
		archivo.close()
	except:
		print ("Error.Copiado del Archivo sshd_config")
	try:

		archivo = open ('sshd_config','w')
		for i in range(len(lines)):
			if 'PermitRootLogin' in lines[i]:
				lines[i] = 'PermitRootLogin yes\n'
			archivo.write (lines[i])
		archivo.close()
	except:
		print("Error.Modificacion del Archivo sshd_config")

sshd_config()