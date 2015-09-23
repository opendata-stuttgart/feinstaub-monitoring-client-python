# monitoring of own sensors on feinstaub-api

## config

set your API_TOKEN (and PUSHOVER tokens) in config.py

(see config.py-template for example)

## run as cron

```
./run.sh
```

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


