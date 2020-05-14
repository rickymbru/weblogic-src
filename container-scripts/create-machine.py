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
machineName=configProps.get("machine.name")

from java.util import Properties

###################################################################

def createMachine():
    # Display the variable values.
    print 'adminUsername=', adminUsername
    print 'adminPassword=', adminPassword
    print 'adminURL=', adminURL
    print 'machineName=', machineName

    try:
        edit()
        startEdit()

        # Machine-1 = the new WebLogic Machine
        cmo.createUnixMachine(machineName)

        cd('/Machines/' + machineName + '/NodeManager/' + machineName)
        cmo.setListenAddress(machineName)

        save();

        activate()

    except:

        print 'Exception while create EMail session!';

        dumpStack();

        exit();    

# ================================================================                                                                                                                          

#           Main Code Execution                                                                                                                                                            

# ================================================================                                                                                                                         

if __name__== "main":    

        print '###################################################################';

        print '#                 Create Machine                                  #';

        print '###################################################################';

        print '';        

        connect(adminUsername, adminPassword,  adminURL);

        createMachine()

        disconnect();  