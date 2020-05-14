#!/bin/sh

docker stop weblogic-12.2.1.4-deploy
sleep 5
docker image rm 12.2.1.4-generic-deploy