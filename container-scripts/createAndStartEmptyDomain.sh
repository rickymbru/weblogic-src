#!/bin/bash
#
#Copyright (c) 2014-2018 Oracle and/or its affiliates. All rights reserved.
#
#Licensed under the Universal Permissive License v 1.0 as shown at https://oss.oracle.com/licenses/upl.


# If AdminServer.log does not exists, container is starting for 1st time
# So it should start NM and also associate with AdminServer
# Otherwise, only start NM (container restarted)
########### SIGTERM handler ############
function _term() {
   echo "Stopping container."
   echo "SIGTERM received, shutting down the server!"
   ${DOMAIN_HOME}/bin/stopWebLogic.sh
}

########### SIGKILL handler ############
function _kill() {
   echo "SIGKILL received, shutting down the server!"
   kill -9 $childPID
}

# Set SIGTERM handler
trap _term SIGTERM

# Set SIGKILL handler
trap _kill SIGKILL

#Define DOMAIN_HOME
export DOMAIN_HOME=/u01/oracle/user_projects/domains/$DOMAIN_NAME
echo "Domain Home is: " $DOMAIN_HOME

ADD_DOMAIN=1
if [ ! -f ${DOMAIN_HOME}/servers/AdminServer/logs/AdminServer.log ]; then
    ADD_DOMAIN=0
fi

mkdir -p $ORACLE_HOME/properties
# Create Domain only if 1st execution
if [ $ADD_DOMAIN -eq 0 ]; then
   PROPERTIES_FILE=/u01/oracle/properties/domain.properties
   if [ ! -e "$PROPERTIES_FILE" ]; then
      echo "A properties file with the username and password needs to be supplied."
      exit
   fi

   # Get Username
   USER=`awk '{print $1}' $PROPERTIES_FILE | grep username | cut -d "=" -f2`
   if [ -z "$USER" ]; then
      echo "The domain username is blank.  The Admin username must be set in the properties file."
      exit
   fi
   # Get Password
   PASS=`awk '{print $1}' $PROPERTIES_FILE | grep password | cut -d "=" -f2`
   if [ -z "$PASS" ]; then
      echo "The domain password is blank.  The Admin password must be set in the properties file."
      exit
   fi

   # Create an empty domain
   wlst.sh -skipWLSModuleScanning -loadProperties $PROPERTIES_FILE  /u01/oracle/create-wls-domain.py
   mkdir -p ${DOMAIN_HOME}/servers/AdminServer/security/
   echo "username=${USER}" >> $DOMAIN_HOME/servers/AdminServer/security/boot.properties
   echo "password=${PASS}" >> $DOMAIN_HOME/servers/AdminServer/security/boot.properties
   ${DOMAIN_HOME}/bin/setDomainEnv.sh
fi

# Rewrite setStartupEnv and startManagedWebLogic.sh
cat /u01/oracle/setStartupEnv.sh >$DOMAIN_HOME/bin/setStartupEnv.sh
cat /u01/oracle/startManagedWebLogic.sh >$DOMAIN_HOME/bin/startManagedWebLogic.sh

# Start Admin Server and tail the logs
nohup ${DOMAIN_HOME}/startWebLogic.sh &
#touch ${DOMAIN_HOME}/servers/AdminServer/logs/AdminServer.log

echo '####################################################################################'
echo Waiting 10 seconds to Weblogic Starts...
echo '####################################################################################'
sleep 15

# Exporting variables
export MW_HOME=/u01/oracle       
export WLS_HOME=$MW_HOME/wlserver
export WL_HOME=$WLS_HOME         
. $DOMAIN_HOME/bin/setDomainEnv.sh

#Create Managed Server
echo Creating Managed Server $SERVER_NAME1 ...
java weblogic.WLST /u01/oracle/create-managed-server.py -p /u01/oracle/server.properties

# Start Managed Server
mkdir -p servers/APP01/security                       
cp /u01/oracle/boot.properties servers/APP01/security/
nohup startManagedWebLogic.sh $SERVER_NAME1 &
echo '####################################################################################'
echo Waiting 15 seconds to Managed Server $SERVER_NAME1 start...
echo '####################################################################################'
sleep 15

# Create Data Source
echo Creating Data Source ...
java weblogic.WLST /u01/oracle/create-data_source.py -p /u01/oracle/ds.properties

# Create Mail Session
echo Creating Mail Session ...
java weblogic.WLST /u01/oracle/create-mail-session.py -p /u01/oracle/mail.properties

# Deploy App
echo Deploying App ...
java weblogic.WLST /u01/oracle/app-deploy.py -p /u01/oracle/app.properties

tail -f ${DOMAIN_HOME}/servers/AdminServer/logs/AdminServer.log &

childPID=$!
wait $childPID
