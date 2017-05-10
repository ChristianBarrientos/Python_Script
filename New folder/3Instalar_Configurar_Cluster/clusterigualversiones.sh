#! /bin/bash

echo "DIRECTORIOS"


mkdir /home/guarani/herramientas

mkdir /home/guarani/herramientas/corosync

mkdir /home/guarani/herramientas/CLUESTER-GLUE

mkdir /home/guarani/herramientas/CRMSH

mkdir /home/guarani/herramientas/LIBQB

mkdir /home/guarani/herramientas/pacemaker

mkdir /home/guarani/herramientas/RESOURCE-AGENTS

mkdir /home/guarani/herramientas/dependencias


echo "Pre-Configuraciones"

 
apt-get install build-essential -y 
if [ "$?" != "0" ]; then echo "build-essential"; exit 1; fi
apt-get install automake autoconf -y
if [ "$?" != "0" ]; then echo "automake "; exit 1; fi
apt-get install pkg-config -y
if [ "$?" != "0" ]; then echo "pkg-config"; exit 1; fi

echo "Dependencias"


apt-get install libnss3-dev -y
if [ "$?" != "0" ]; then echo "libnss3-dev"; exit 1; fi
apt-get install groff -y
if [ "$?" != "0" ]; then echo "groff "; exit 1; fi 
apt-get install rpm -y
if [ "$?" != "0" ]; then echo "rpm"; exit 1; fi

apt-get install libcpg-dev -y

if [ "$?" != "0" ]; then echo "libcpg-dev"; exit 1; fi

apt-get install uuid-dev -y

if [ "$?" != "0" ]; then echo "uuid-dev "; exit 1; fi

apt-get install libglib2.0-dev -y
if [ "$?" != "0" ]; then echo "libglib2.0"; exit 1; fi
apt-get install libxml2-dev -y
if [ "$?" != "0" ]; then echo "libxml2"; exit 1; fi
apt-get install libxslt1-dev -y
if [ "$?" != "0" ]; then echo "libxslt1"; exit 1;fi
apt-get install libcfg-dev -y 
if [ "$?" != "0" ]; then echo "libcfg-dev"; exit 1; fi 
apt-get install libbz2-dev -y 
if [ "$?" != "0" ];then echo "libbz2"; exit 1; fi 
apt-get install libncurses5-dev -y 
if ["$?" != "0" ]; then echo "libncurses5"; exit 1; fi 
apt-get install libaio-dev -y 
if [ "$?" != "0" ]; then echo "libaio-dev"; exit 1; fi 
apt-get install libtool-bin -y
if [ "$?" != "0" ]; then echo"libtool-bin"; exit 1; fi
apt-get install python-lxml -y
if [ "$?" != "0" ]; then echo"python"; exit 1; fi

#descaga-instala
#cd /home/guarani/herramientas/dependencias
#wget https://github.com/ClusterLabs/libqb/archive/v0.17.2.zip
#if [ "$?" != "0" ]; then echo "Bajando Libqb"; exit 1; fi
#unzip v0.17.2.zip
#if [ "$?" != "0" ]; then echo "Unzip Libqb"; exit 1; fi
#cd /home/guarani/herramientas/dependencias/libqb-0.17.2
#./autogen.sh
#if [ "$?" != "0" ]; then echo "AUTOGEN Libqb"; exit 1; fi
#./configure
#if [ "$?" != "0" ]; then echo "CONFIGURE Libqb"; exit 1; fi
#make
#if [ "$?" != "0" ]; then echo "MAKE Libqb"; exit 1; fi
#make install
#if [ "$?" != "0" ]; then echo "MAKE INSTALL Libqb"; exit 1; fi

cd /home/guarani/herramientas/dependencias
wget ftp://ftp.gnu.org/pub/gnu/libtool/libtool-2.4.2.tar.gz
tar xvzf libtool-2.4.2.tar.gz
cd /home/guarani/herramientas/dependencias/libtool-2.4.2
./configure
if [ "$?" != "0" ]; then echo "configure libtool"; exit 1; fi
make
if [ "$?" != "0" ]; then echo "make libtool"; exit 1; fi
make install
if [ "$?" != "0" ]; then echo  "make install libtool"; exit 1; fi




echo "LIBQB"


cd /home/guarani/herramientas/LIBQB
wget https://github.com/ClusterLabs/libqb/archive/v0.17.2.zip
unzip v0.17.2.zip
cd /home/guarani/herramientas/LIBQB/libqb-0.17.2
echo "0.17.0" > .tarball-version
./autogen.sh
if [ "$?" != "0" ]; then echo "autogen LIBQB"; exit 1; fi
./configure
if [ "$?" != "0" ]; then echo "configure LIBQB"; exit 1; fi
 make
if [ "$?" != "0" ]; then echo  "make LIBQB"; exit 1; fi
make install



echo "COROSYNC"
sleep 2

cd /home/guarani/herramientas/corosync
wget https://github.com/corosync/corosync/archive/v2.3.3.zip
unzip v2.3.3.zip
cd /home/guarani/herramientas/corosync/corosync-2.3.3 
echo "2.3.3" > .tarball-version
./autogen.sh
 if [ "$?" != "0" ]; then echo "autogen COROSYNC "; exit 1; fi 
./configure 
if [ "$?" != "0" ]; then echo "configure COROSYNC "; exit 1; fi
 make
if [ "$?" != "0" ]; then echo "make COROSYNC" ; exit 1; fi
make install


echo "CLUESTER-GLUE"


cd /home/guarani/herramientas/CLUESTER-GLUE
wget  http://hg.linux-ha.org/glue/archive/glue-1.0.12.tar.bz2
tar xvjf glue-1.0.12.tar.bz2
cd /home/guarani/herramientas/CLUESTER-GLUE/Reusable-Cluster-Components-glue--glue-1.0.12
./autogen.sh
if [ "$?" != "0" ]; then echo "autogen Cluster-GLUE" ; exit 1; fi
./configure
if [ "$?" != "0" ]; then echo "configure Cluster-GLUE" ; exit 1; fi
make
if [ "$?" != "0" ]; then echo "configure Cluster-GLUE" ; exit 1; fi
make install 


echo "RESOURCE-AGENTS"



cd /home/guarani/herramientas/RESOURCE-AGENTS
wget https://github.com/ClusterLabs/resource-agents/archive/v3.9.5.zip
unzip v3.9.5.zip
cd /home/guarani/herramientas/RESOURCE-AGENTS/resource-agents-3.9.5
echo "3.9.5" > .tarball-version
./autogen.sh
if [ "$?" != "0" ]; then echo "autogen RESOURCE-AGENTS "; exit 1; fi 
./configure
if [ "$?" != "0" ]; then echo "configure RESOURCE-AGENTS "; exit 1; fi 
make
if [ "$?" != "0" ]; then echo "make RESOURCE-AGENTS"; exit 1; fi
make install

echo "PACEMAKER"


cd /home/guarani/herramientas/pacemaker
wget https://github.com/ClusterLabs/pacemaker/archive/Pacemaker-1.1.14.zip
unzip Pacemaker-1.1.14.zip
cd /home/guarani/herramientas/pacemaker/pacemaker-Pacemaker-1.1.14 
addgroup --system haclient
if [ "$?" != "0" ]; then echo "grupo PACEMAKER "; exit 1; fi
adduser --system --no-create-home --ingroup haclient hacluster
if [ "$?" != "0" ]; then echo "usuario PACEMAKER "; exit 1; fi 
./autogen.sh
if [ "$?" != "0" ]; then echo "autogen PACEMAKER "; exit 1; fi
./configure 
if [ "$?" != "0" ]; then echo "configure PACEMAKER "; exit 1; fi
make
if [ "$?" != "0" ]; then echo "make PACEMAKER"; exit 1; fi
make install


echo "CRMSH"


cd /home/guarani/herramientas/CRMSH
wget https://github.com/ClusterLabs/crmsh/archive/2.2.0.zip
unzip 2.2.0.zip
cd /home/guarani/herramientas/CRMSH/crmsh-2.2.0
./autogen.sh 
if [ "$?" != "0" ]; then echo "autogen CRMSH"; exit 1; fi 
./configure
if [ "$?" != "0" ]; then echo "configure CRMSH"; exit 1; fi 
make
if [ "$?" != "0" ]; then echo  "make CRMSH"; exit 1; fi
make install


echo "EMPIEZA CONFIGURACION CLUSTER ------"
sleep 5

chmod 777 scriptconfiguracioncluster.sh
./scriptconfiguracioncluster.sh
