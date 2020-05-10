#!/bin/sh
./build.sh
docker run --rm -d -p 7001:7001 -p 9002:9002 \
-e ADMINISTRATION_PORT_ENABLED=false \
-v /home/docker/weblogic-src/properties/:/u01/oracle/properties \
-v /home/docker/weblogic-src/weblogic-external:/var/weblogic-external \
-v /home/docker/weblogic-src/weblogic-external-data:/var/weblogic-external-data \
--name weblogic-12.2.1.4-srcds 12.2.1.4-generic-srcds

docker logs weblogic-12.2.1.4-srcds -t -f

