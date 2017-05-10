#! /bin/bash

python corosyncconfig.py
if [ "$?" != "0" ]; then echo "corosyncconfig.py"; exit 1; fi
python corosyncdefaultstart.py
if [ "$?" != "0" ]; then echo "corosyncdefaultstart.py"; exit 1; fi
python corosyncservicepcmk.py
if [ "$?" != "0" ]; then echo "corosyncservicepcmk.py"; exit 1; fi
 

mv corosync.conf /etc/corosync/
mv corosync /etc/default/
mv pcmk /etc/corosync/service.d/

echo "GENERAR LLAVE COROSYNC---------------------"
sleep 4
corosync-keygen 

scp /etc/corosync/keygen root@912.168.179.22:/etc/corosync 

