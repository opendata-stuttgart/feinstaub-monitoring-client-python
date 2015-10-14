# monitoring of own sensors on feinstaub-api

## config

set your API_TOKEN (and PUSHOVER tokens) in config.py

(see config.py-template for example)

## run as cron

add to your crontab:

```
*/5 * * * * (cd /your_path_to/feinstaub-monitoring-client-python; bash ./run.sh > /dev/null)
```

## virtualenv

```
cp config.py-template config.py
# edit config.py
mkvirtualenv feinstaub-api-client -p /usr/bin/python3
pip install -r requirements.txt
python monitor.py
deactivate
# re-enter
workon feinstaub-api-client
```
# checking clients on Freifunk (ff) router

* You need key based ssh access to your router
* Be connected via Freifunk
* then get a list of clients with

    ./ffrouterclients.sh

If you have a file chipids.csv then the MAC will be grepped there

~~~
chipid	name	label dustiID	MAC
10673656	mysensor1	ESP1	155	18:fe:34:f4:aa:aa
~~~

# get data and process to csv

copy config.sh.template to config.sh and change the variable values in there, then run the ./getdata.sh script to download all data for the sensors into files, see result dir dusti.sensordata.<date>.<XXXX> for them.
The script ./assembledatafromjson.py assembles a csv from the json files specified on commandline (e.g. dusti.sensordata.2015-10-14.z6OU/00/*.json)



