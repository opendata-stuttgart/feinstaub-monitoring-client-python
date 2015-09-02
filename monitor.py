import requests
import datetime
from config import API_TOKEN


def check():
    header = {'Authorization': 'Token ' + API_TOKEN}
    session = requests.Session()
    url = "https://api.dusti.xyz/v1/node/"
    r = session.get(url, headers=header)
    for node in r.json():
        if node.get("last_data_push"):
            last_data_push = datetime.datetime.strptime(node.get("last_data_push")[:19],
                                                        "%Y-%m-%dT%H:%M:%S")
            print(last_data_push)
            # TODO:
            # check if not older that 1h
            # check if older than 5min
            # if both; send message to owner
            # - mail
            # - push (i.e. pushover)


check()
