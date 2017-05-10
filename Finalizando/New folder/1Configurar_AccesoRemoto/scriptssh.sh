#! /bin/bash




ip=192.168.179.22 



ssh-keygen -P ''


if [ "$?" != "0" ]; then echo "ssh-keygen"; exit 1; fi



ssh-copy-id -i ~/.ssh/id_rsa.pub $ip

