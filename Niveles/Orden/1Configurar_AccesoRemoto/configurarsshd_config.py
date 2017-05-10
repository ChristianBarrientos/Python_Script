
archivo = open ('/etc/ssh/sshd_config','r')

lines = list(archivo)

archivo.close()

archivo = open ('sshd_config','w')
for i in range(len(lines)):
	if 'PermitRootLogin' in lines[i]:
		lines[i] = 'PermitRootLogin yes\n'
	archivo.write (lines[i])
archivo.close()

