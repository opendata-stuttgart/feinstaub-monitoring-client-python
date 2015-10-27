#!/usr/bin/env python
import requests
import datetime
import click
import os
import os.path
from config import (
    API_TOKEN,
    LAST_N_HOURS,
    LAST_N_MINUTES,
    PUSHOVER_API_TOKEN,
    PUSHOVER_CLIENT_TOKEN,
)
from pushover import Client


locks_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'locks')


def check_file(sensor_id):
    fn = os.path.join(locks_directory, '{}.lock'.format(sensor_id))
    if os.path.isfile(fn):
        with open(fn) as fp:
            s = fp.readline().strip()
        return datetime.datetime.strptime(s, "%Y-%m-%dT%H:%M:%S")
    return False


def update_file(sensor_id, timestamp):
    fn = os.path.join(locks_directory, '{}.lock'.format(sensor_id))
    with open(fn, 'w') as fp:
        fp.write("{}\n".format(timestamp.isoformat()))


def delete_file(sensor_id):
    fn = os.path.join(locks_directory, '{}.lock'.format(sensor_id))
    if os.path.isfile(fn):
        os.remove(fn)


@click.command()
@click.option('--push/--no-push', default=False)
@click.option('--show/--no-show', default=True)
def check(push, show):
    header = {'Authorization': 'Token ' + API_TOKEN}
    session = requests.Session()
    url = "https://api.dusti.xyz/v1/node/"
    r = session.get(url, headers=header)
    if push:
        client = Client(PUSHOVER_CLIENT_TOKEN, api_token=PUSHOVER_API_TOKEN)
    for node in r.json():
        if node.get("last_data_push"):
            last_data_push = datetime.datetime.strptime(node.get("last_data_push")[:19],
                                                        "%Y-%m-%dT%H:%M:%S")
            sensor_id = node.get('sensors', [{}])[0].get('id')
            last_check_timestamp = check_file(sensor_id)
            if (last_data_push < datetime.datetime.utcnow() - datetime.timedelta(minutes=LAST_N_MINUTES) and
                last_data_push > datetime.datetime.utcnow() - datetime.timedelta(hours=LAST_N_HOURS)):
                uid = node.get('uid')
                description = node.get('sensors', [{}])[0].get('description')
                if show:
                    click.echo("{} | {:>35} | {}".format(last_data_push, uid, description))
                if not last_check_timestamp:
                    if push:
                        client.send_message("sensor: {}\ndescription: {}".format(uid, description),
                                            title="Sensor hasn't pushed in the last 5 minutes!")
                        # FIXME: calculate moment of last push and add into message
                update_file(sensor_id, last_data_push)
            elif last_check_timestamp:
                delete_file(sensor_id)
                if push:
                    client.send_message("RESTORED sensor: {}\ndescription: {}".format(uid, description),
                                        title="Sensor is back again!")

if __name__ == '__main__':
    check()
