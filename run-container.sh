#!/bin/sh
./build.sh
docker run --rm -d -p 7001:7001 -p 7003:7003 -p 9002:9002 \
-e ADMINISTRATION_PORT_ENABLED=false \
-e DOMAIN_NAME=base_domain \
-e SERVER_NAME1=APP01 \
-v /home/docker/weblogic-src/properties/:/u01/oracle/properties \
-v /home/docker/weblogic-src/weblogic-external:/var/weblogic-external \
-v /home/docker/weblogic-src/weblogic-external-data:/var/weblogic-external-data \
--name weblogic-12.2.1.4-deploy 12.2.1.4-generic-deploy

docker logs weblogic-12.2.1.4-deploy -t -f

