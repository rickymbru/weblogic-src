#!/bin/sh

docker stop weblogic-12.2.1.4-srcds
sleep 5
docker image rm 12.2.1.4-generic-srcds