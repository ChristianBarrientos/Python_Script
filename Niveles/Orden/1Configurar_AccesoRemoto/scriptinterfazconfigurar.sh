#! /bin/bash

python interfaces.py
if [ "$?" != "0" ]; then echo "interfaces.py"; exit 1; fi

mv interfaces /etc/network/

chmod 777 scriptpermitrootloggin.sh
chmod 777 scriptssh.sh

./scriptpermitrootloggin.sh
./scriptssh.sh