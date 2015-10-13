#!/bin/sh
docker build --tag=feinstaub-monitor-client .
## add -ti when running in a shell and not as a cron
docker run --rm --volume `pwd`/locks:/opt/code/locks --name feinstaub-monitor-client-run feinstaub-monitor-client
