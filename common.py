import os
import csv
import json
import subprocess
from config import *


def get_torrents():
    process = subprocess.Popen(GET_TORRENTS_LIST.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    return json.loads(output.decode('utf-8'))


def get_torrents_by_category(torrents: list, category: str):
    for torrent in torrents:
        if torrent['category'] == category:
            yield torrent


def get_torrents_by_tag(torrents: list, tag: str):
    for torrent in torrents:
        if tag:
            if tag in torrent['tags']:
                yield torrent
        else: # tag is ''
            if not torrent['tags']:
                yield torrent


def write_torrent_info(torrent: dict):
    if not os.path.isfile(TORRENTS_CSV):
        items = ['name', 'size', 'ratio', 'finished']
        with open(TORRENTS_CSV, 'w') as f:
            writer = csv.DictWriter(f, fieldnames=items)
            writer.writeheader()
    with open(TORRENTS_CSV, 'a') as f:
        writer = csv.writer(f)
        writer.writerow([
            torrent['name'],
            torrent['size'],
            torrent['ratio'],
            torrent['progress'] == 1.0
        ])
