# monitoring of own sensors on feinstaub-api

## config

set your API_TOKEN (and PUSHOVER tokens) in config.py

(see config.py-template for example)

## run as cron

```
./run.sh
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


