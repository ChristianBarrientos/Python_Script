


archivo = open('interfaces','w')

ip = "192.168.179.21"
mascara = "255.255.255.0"
puerta_enlace = "192.168.179.2"

archivo.write("# This file describes the network interfaces available on your system\n")
archivo.write("# and how to activate them. For more information, see interfaces(5).\n")
archivo.write("\n")
archivo.write("source /etc/network/interfaces.d/*\n")
archivo.write("\n")
archivo.write("# The loopback network interface\n")
archivo.write("auto lo\n")
archivo.write("iface lo inet loopback\n")
archivo.write("\n")
archivo.write("allow-hotplug eth0\n")
archivo.write("iface eth0 inet static\n")
archivo.write("address "+ip+"\n")
archivo.write("netmask "+mascara+"\n")
archivo.write("gateway "+puerta_enlace+"\n")
