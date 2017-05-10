#! /bin/bash

cd /home/guarani/pasaradebian
python corosyncconfig.py
python defaultcorosyncpcmk.py

cd /home/guarani/archivos
mv corosync.conf /etc/corosync/
mv pcmk /etc/corosync/service.d/

