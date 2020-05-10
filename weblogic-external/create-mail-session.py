# ................  import ........................

from java.util import Properties

###################################################################

def createMailSession():                                                                                                                                                                    

    try:

        print 'Create EMail session ...';

        edit();

        startEdit();

 

        cd('/')

        myTestMailMbean = cmo.createMailSession('cedaeMailSession');

        cd('/MailSessions/cedaeMailSession');

        set('Targets',jarray.array([ObjectName('com.bea:Name=AdminServer,Type=Server')], ObjectName))

        myTestMailMbean.setJNDIName('mail/cedaeMailSession'); 

        properties = java.util.Properties();

        properties.put('mail.smtp.connectiontimeout','10000');

        properties.put('mail.smtp.timeout','1000');

        properties.put('mail.transport.protocol','smtp');

        properties.put('mail.smtp.host','smtp.cedae.corp');

        properties.put('mail.smtp.port','25');

        myTestMailMbean.setProperties(properties);

        save();

        activate(); 

    except:

        print 'Exception while create EMail session  !';

        dumpStack();

        exit();

 

 

# ================================================================                                                                                                                          

#           Main Code Execution                                                                                                                                                            

# ================================================================                                                                                                                         

if __name__== "main":                                                                                                                                                                       

        print '###################################################################';

        print '#                 Test create Mail session                        #';

        print '###################################################################';

        print '';

        connect('admin', 'Welcome1',  't3://localhost:7001');

        createMailSession()

        disconnect();  