#!/bin/bash

export PATH=$PATH:$ORACLE_HOME/bin
export ORACLE_SID=ORCLCDB

#sqlplus / as sysdba @$ORACLE_BASE/scripts/startup/create-src
impdp "'/ as sysdba'" directory=DATA_PUMP_DIR schemas=SRC dumpfile=src-12.1.dmp logfile=src-12.1.log 