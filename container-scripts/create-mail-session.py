#!/usr/bin/python
# Author : Ricky
# Save Script as : create-mail-session.py

import time
import getopt
import sys
import re

# Get location of the properties file.
properties = ''
try:
   opts, args = getopt.getopt(sys.argv[1:],"p:h::",["properies="])
except getopt.GetoptError:
   print 'set_datasource.py -p <path-to-properties-file>'
   sys.exit(2)
for opt, arg in opts:
   if opt == '-h':
      print 'set_datasource.py -p <path-to-properties-file>'
      sys.exit()
   elif opt in ("-p", "--properties"):
      properties = arg
print 'properties=', properties

# Load the properties from the properties file.
from java.io import FileInputStream
 
propInputStream = FileInputStream(properties)
configProps = Properties()
configProps.load(propInputStream)

# Set all variables from values in properties file.
adminUsername=configProps.get("admin.username")
adminPassword=configProps.get("admin.password")
adminURL=configProps.get("admin.url")
mailName=configProps.get("mail.name")
mailJNDIName=configProps.get("mail.jndi.name")
mailconnectiontimeout=configProps.get("mail.smtp.connectiontimeout")
mailtimeout=configProps.get("mail.smtp.timeout")
mailprotocol=configProps.get("mail.transport.protocol")
mailhost=configProps.get("mail.smtp.host")
mailport=configProps.get("mail.smtp.port")
mailTargetType=configProps.get("mail.target.type")
mailTargetName=configProps.get("mail.target.name")

from java.util import Properties

###################################################################

def createMailSession():
   # Display the variable values.
   print 'adminUsername=', adminUsername
   print 'adminPassword=', adminPassword
   print 'adminURL=', adminURL

   try:

      print 'Create EMail session ...';

      edit();

      startEdit();

      cd('/')
      myTestMailMbean = cmo.createMailSession(mailName);

      cd('/MailSessions/' + mailName);

      set('Targets',jarray.array([ObjectName('com.bea:Name=' + mailTargetName + ',Type=' + mailTargetType)], ObjectName))

      myTestMailMbean.setJNDIName(mailJNDIName); 

      properties = java.util.Properties();

      properties.put('mail.smtp.connectiontimeout',mailconnectiontimeout);

      properties.put('mail.smtp.timeout',mailtimeout);

      properties.put('mail.transport.protocol',mailprotocol);

      properties.put('mail.smtp.host',mailhost);

      properties.put('mail.smtp.port',mailport);

      myTestMailMbean.setProperties(properties);

      save();

      activate(); 

   except:

      print 'Exception while create EMail session!';

      dumpStack();

      exit();

# ================================================================                                                                                                                          

#           Main Code Execution                                                                                                                                                            

# ================================================================                                                                                                                         

if __name__== "main":                                                                                                                                                                       

        print '###################################################################';

        print '#                 Create Mail session                        #';

        print '###################################################################';

        print '';

        connect(adminUsername, adminPassword,  adminURL);

        createMailSession()

        disconnect();  