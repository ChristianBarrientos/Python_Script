
archivo = open ("corosyncconfig.txt",'w')

cantidad_nodos = 7
direcciones = ['192.168.179.1','192.168.179.2','192.168.179.3','192.168.179.4','192.168.179.5','192.168.179.6','192.168.179.7']


archivo.write("nodelist {\n")
archivo.write("\n")

#for i in range(1, 6):

for i in range(0,cantidad_nodos):

#cadena ='\t\tring0_addr: %s \n' %(direcciones[1])
	archivo.write("\tnode {\n")
	archivo.write("\n")
	archivo.write('\t\tring0_addr: %s \n' %(direcciones[i]))
	archivo.write("\t\t#nodeid: %c\n"%(i))
	archivo.write("\t}\n")

#print cadena