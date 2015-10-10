#!/bin/sh
docker build --tag=feinstaub-monitor-client .
docker run --rm -ti --volume `pwd`/locks:/opt/code/locks --name feinstaub-monitor-client-run feinstaub-monitor-client
