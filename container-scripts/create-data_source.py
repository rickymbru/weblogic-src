#!/usr/bin/python
# Author : Tim Hall
# Save Script as : create_data_source.py

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
dsName=configProps.get("ds.name")
dsJNDIName=configProps.get("ds.jndi.name")
dsURL=configProps.get("ds.url")
dsDriver=configProps.get("ds.driver")
dsUsername=configProps.get("ds.username")
dsPassword=configProps.get("ds.password")
dsTargetType=configProps.get("ds.target.type")
dsTargetName=configProps.get("ds.target.name")
dsTargetAdmin=configProps.get("ds.target.admin")

###################################################################

def createDataSource():
# Display the variable values.
   print 'adminUsername=', adminUsername
   print 'adminPassword=', adminPassword
   print 'adminURL=', adminURL
   print 'dsName=', dsName
   print 'dsJNDIName=', dsJNDIName
   print 'dsURL=', dsURL
   print 'dsDriver=', dsDriver
   print 'dsUsername=', dsUsername
   print 'dsPassword=', dsPassword
   print 'dsTargetType=', dsTargetType
   print 'dsTargetName=', dsTargetName
   print 'dsTargetAdmin=', dsTargetAdmin

   try:

      edit()
      startEdit()

      # Create data source.
      cd('/')
      cmo.createJDBCSystemResource(dsName)

      cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName)
      cmo.setName(dsName)

      cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDataSourceParams/' + dsName)
      set('JNDINames',jarray.array([String(dsJNDIName)], String))

      cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDriverParams/' + dsName)
      cmo.setUrl(dsURL)
      cmo.setDriverName(dsDriver)
      set('Password', dsPassword)

      cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCConnectionPoolParams/' + dsName)
      cmo.setTestTableName('SQL SELECT 1 FROM DUAL\r\n\r\n')

      cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDriverParams/' + dsName + '/Properties/' + dsName)
      cmo.createProperty('user')

      cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDriverParams/' + dsName + '/Properties/' + dsName + '/Properties/user')
      cmo.setValue(dsUsername)

      cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDataSourceParams/' + dsName)
      cmo.setGlobalTransactionsProtocol('TwoPhaseCommit')

      cd('/SystemResources/' + dsName)
      #set('Targets',jarray.array([ObjectName('com.bea:Name=' + dsTargetName + ',Type=' + dsTargetType)], ObjectName))
      jdbcDS1=cmo
      cd("/Servers/" + dsTargetName)
      target=cmo  
      jdbcDS1.addTarget(target)
      cd("/Servers/" + dsTargetAdmin)
      target=cmo  
      jdbcDS1.addTarget(target)

      save()
      activate()

      disconnect()
      exit()

   except:
      print 'Exception while create Data Source!';

      dumpStack();

      exit();      


if __name__== "main":                                                                                                                                                                       

        print '###################################################################';

        print '#                 Create Data Source                              #';

        print '###################################################################';

        print '';

        connect(adminUsername, adminPassword,  adminURL);

        createDataSource()

        disconnect();