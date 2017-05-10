
archivo = open ("corosync.conf",'w')

bindnetaddr= "192.168.179.0"
cantidad_nodos = 2
direcciones = ['192.168.179.1','192.168.179.2','192.168.179.3','192.168.179.4','192.168.179.5','192.168.179.6','192.168.179.7']



archivo.write("# Please read the openais.conf.5 manual page\n")

archivo.write("totem {\n")
archivo.write("\n")
archivo.write("\tversion: 2\n")

        # How long before declaring a token lost (ms)
archivo.write("\ttoken: 3000\n")

        # How many token retransmits before forming a new configuration
archivo.write("\ttoken_retransmits_before_loss_const: 10\n")

        # How long to wait for join messages in the membership protocol (ms)
archivo.write("\tjoin: 60\n")

        # How long to wait for consensus to be achieved before starting a new ro$
archivo.write("\tconsensus: 3600\n")

        # Turn off the virtual synchrony filter
archivo.write("\tvsftype: none\n")

        # Number of messages that may be sent by one processor on receipt of the$
archivo.write("\tmax_messages: 20\n")

        # Limit generated nodeids to 31-bits (positive signed integers)
archivo.write("\tclear_node_high_bit: yes\n")

        # Disable encryption
archivo.write("\tsecauth: off\n")

        # How many threads to use for encryption/decryption
archivo.write("\tthreads: 0\n")

        # Optionally assign a fixed node id (integer)
      # This specifies the mode of redundant ring, which may be none, active, $
archivo.write("\trrp_mode: none\n")

archivo.write("\n")
archivo.write("\n")
archivo.write("\n")
archivo.write("\tinterface {\n")
archivo.write("\n")# The following values need to be set based on your environment
archivo.write("\t\tringnumber: 0\n")
archivo.write("\t\tbindnetaddr: %s \n"%(bindnetaddr))
archivo.write("\t\tmcastaddr: 226.94.1.1\n")
archivo.write("\t\tmcastport: 5405\n")
archivo.write("\t}\n")
archivo.write("}\n")
archivo.write("\n")
archivo.write("amf {\n")
archivo.write("\n")
archivo.write("\tmode: disabled\n")
archivo.write("}\n")
archivo.write("\n")
archivo.write("service {\n")
archivo.write("\n")
archivo.write("\n")      # Load the Pacemaker Cluster Resource Manager
archivo.write("\tver:       0\n")
archivo.write("\tname:      pacemaker\n")
archivo.write("}\n")
archivo.write("\n")
archivo.write("aisexec {\n")
archivo.write("\n")
archivo.write("\tuser:   root\n")
archivo.write("\tgroup:  root\n")
archivo.write("}\n")
archivo.write("\n")
archivo.write("logging {\n")
archivo.write("\n")
archivo.write("\tfileline: off\n")
archivo.write("\tto_stderr: yes\n")
archivo.write("\tto_logfile: no\n")
archivo.write("\tto_syslog: yes\n")
archivo.write("\tsyslog_facility: daemon\n")
archivo.write("\tdebug: off\n")
archivo.write("\ttimestamp: on\n")
archivo.write("\tlogger_subsys {\n")
archivo.write("\n")
archivo.write("\t\tsubsys: AMF\n")
archivo.write("\t\tdebug: off\n")
archivo.write("\t\ttags: enter|leave|trace1|trace2|trace3|trace4|trace6\n")
archivo.write("\t}\n")
archivo.write("\n")
archivo.write("\n")
archivo.write("}\n")


archivo.write("nodelist {\n")
archivo.write("\n")
for i in range(0,cantidad_nodos):
    archivo.write("\tnode {\n")
    archivo.write("\n")
    archivo.write('\t\tring0_addr: %s \n' %(direcciones[i]))
    archivo.write("\t\t#nodeid: %c\n"%(i))
    archivo.write("\t}\n")
archivo.write("}\n")
archivo.write("\n")
#archivo.write("nodelist {\n")
#archivo.write("\n")
#archivo.write("\tnode {\n")
#archivo.write("\n")
#archivo.write("\t\tring0_addr: 192.168.15.128\n")
#archivo.write("\t\t#nodeid: 1\n")
#archivo.write("\t}\n")

#archivo.write("\n")
#archivo.write("\tnode {\n")
#archivo.write("\n")
#archivo.write("\t\tring0_addr: 192.168.15.158\n")
#archivo.write("\t\t#nodeid: 2\n")
#archivo.write("\t}\n")
#archivo.write("}\n")
#archivo.write("\n")

archivo.write("quorum {\n")
archivo.write("\n")
archivo.write("\tEnable and configure quorum subsystem (default: off)\n")
archivo.write("\tsee also corosync.conf.2 and votequorum.2\n")
archivo.write("\tprovider: corosync_votequorum\n")
archivo.write("}\n")




