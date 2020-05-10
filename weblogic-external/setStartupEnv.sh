#!/bin/sh

# WARNING: This file is created by the Configuration Wizard.
# Any changes to this script may be lost when adding extensions to this configuration.

# *************************************************************************
#   Server scoped startup configuration.
# *************************************************************************

# Associate all admin-server server-groups to AdminServerStartupGroup

if [ "${STARTUP_GROUP}" != "" ] ; then
        if [ "${STARTUP_GROUP}" = "BASE-WLS-ADMIN-SVR" ] ; then
                STARTUP_GROUP="AdminServerStartupGroup"
                export STARTUP_GROUP
        fi
fi

# Associate server with a startup group

if [ "${STARTUP_GROUP}" = "" ] ; then
        if [ "${SERVER_NAME}" = "AdminServer" ] ; then
                STARTUP_GROUP="AdminServerStartupGroup"
                export STARTUP_GROUP
        fi
fi

# PRE_CLASSPATH.                                                        
if [ "${PRE_CLASSPATH}" != "" ] ; then                                  
   PRE_CLASSPATH="${PRE_CLASSPATH}${CLASSPATHSEP}/var/weblogic-external"
   export PRE_CLASSPATH                                                 
else                                                                    
   PRE_CLASSPATH="/var/weblogic-external"                               
   export PRE_CLASSPATH                                                 
fi  