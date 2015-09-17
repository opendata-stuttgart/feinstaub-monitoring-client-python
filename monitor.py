import requests
import datetime
import click
from config import API_TOKEN, PUSHOVER_CLIENT_TOKEN, PUSHOVER_API_TOKEN
from pushover import Client


@click.command()
@click.option('--push/--no-push', default=False)
@click.option('--show/--no-show', default=True)
def check(push, show):
    header = {'Authorization': 'Token ' + API_TOKEN}
    session = requests.Session()
    url = "https://api.dusti.xyz/v1/node/"
    r = session.get(url, headers=header)
    for node in r.json():
        if node.get("last_data_push"):
            last_data_push = datetime.datetime.strptime(node.get("last_data_push")[:19],
                                                        "%Y-%m-%dT%H:%M:%S")
            if last_data_push < datetime.datetime.utcnow() - datetime.timedelta(minutes=5):
                if last_data_push > datetime.datetime.utcnow() - datetime.timedelta(hours=1):
                    uid = node.get('uid')
                    description = node.get('sensors', [{}])[0].get('description')
                    if push:
                        client = Client(PUSHOVER_CLIENT_TOKEN, api_token=PUSHOVER_API_TOKEN)
                        client.send_message("sensor: {}\ndescription: {}".format(uid, description),
                                            title="Sensor hasn't pushed in the last 5 minutes!")
                    if show:
                        click.echo("{} | {:>35} | {}".format(last_data_push, uid, description))

if __name__ == '__main__':
    check()
