import os
#import subprocess

direcciones=['192.168.179.128','192.168.179.139']




def ssh_key_copy_id(cont,cantidadnodo):
	
	os.system("ssh-keygen -P ''")

	

	for i in range(0,cantidadnodo):
		print(cont,"valor de CONT")
		print (i,"valor de i")
		if(cont != i):
			print("PASDA"+str(i))
			os.system("ssh-copy-id -i ~/.ssh/id_rsa.pub "+direcciones[i])
			

	print ("yes")
	cont =+1
	if(cont == cantidadnodo):
		print("terminaaa")
		return 0
	else:
		print("conexion con dos")
		os.system("ssh "+direcciones[cont])
		print("genera llave 2")
		os.system("ssh-keygen -P ''")
		print ("yLLEGOOOOOOOOOOOOO")
		os.system("ssh-copy-id -i ~/.ssh/id_rsa.pub "+direcciones[1])

		return 0
		ssh_key_copy_id(cont,cantidadnodo)

ssh_key_copy_id(0,2)

print("finmnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn")



#def sub():
#	direcciones=['192.168.179.137'],
#	proc = subprocess.Popen(['ssh-keygen', '-P'," ''"],  stdin=subprocess.PIPE, stdout=subprocess.PIPE)
#	proc.communicate(stdout('\n')


