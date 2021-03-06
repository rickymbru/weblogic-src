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
appname=configProps.get("app.name")
appfile=configProps.get("app.file")
appdir=configProps.get("app.dir")
apptargetname=configProps.get("app.target.name")
apptargetadmin=configProps.get("app.target.admin")

def deployApp():
   # Display the variable values.
   print 'adminUsername=', adminUsername
   print 'adminPassword=', adminPassword
   print 'adminURL=', adminURL
   print 'appname=', appname
   print 'appfile=', appfile
   print 'appdir=', appdir
   print 'apptargetname=', apptargetname
   print 'apptargetadmin=', apptargetadmin

   try:   
      deploy(appname, appdir + '/' + appfile, targets=apptargetname)
      deploy(appname, appdir + '/' + appfile, targets=apptargetadmin)
   
   except:
      print 'Exception while deploying App !';

      dumpStack();

      exit();

# ================================================================                                                                                                                          

#           Main Code Execution                                                                                                                                                            

# ================================================================                                                                                                                         

if __name__== "main":                                                                                                                                                                       

      print '###################################################################';

      print '#                 Deploying App                                   #';

      print '###################################################################';

      print '';

      connect(adminUsername, adminPassword,  adminURL);

      deployApp()

      disconnect();  

