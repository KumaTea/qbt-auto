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
