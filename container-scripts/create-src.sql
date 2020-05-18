alter session set "_oracle_script"=true;
CREATE OR REPLACE DIRECTORY "DATA_PUMP_DIR" AS '/dmp';
create user src identified by src;
grant connect, resource to src;
exit;