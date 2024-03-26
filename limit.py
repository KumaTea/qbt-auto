"""
Check torrents peers info
If a torrent only downloads and doesn't upload
Limit its speed to 512KiB/s
"""

from config import CAT, KiB, MiB
from session import logging, qbt
from common import get_torrents_by_category, get_torrents_by_tag


THRESHOLD = 64 * KiB
LIMIT = 1 * MiB


def add_limit():
    torrents = get_torrents_by_tag(
        get_torrents_by_category(
            qbt.torrents.info.all(),
            category=CAT
        ),
        tag=None
    )
    no_limit_torrents = [
        torrent for torrent in torrents
        if 'downloading' in torrent['state'] and not torrent['dl_limit']
    ]

    to_limit = []
    for torrent in no_limit_torrents:
        dl_speed = torrent['dlspeed']
        up_speed = torrent['upspeed']
        # if dl_speed > 0 and up_speed == 0:
        # if dl_speed and not up_speed:
        if dl_speed and up_speed < THRESHOLD:  # and torrent['ratio'] < 0.1:
            to_limit.append(torrent)

    if to_limit:
        for torrent in to_limit:
            torrent.setDownloadLimit(LIMIT)
            message = 'LIMIT +\t: `{}`'.format(torrent['name'])
            logging.warning(message)

    return to_limit


def remove_limit():
    torrents = get_torrents_by_tag(
        get_torrents_by_category(
            qbt.torrents.info.all(),
            category=CAT
        ),
        tag=None
    )
    has_limit_torrents = [
        torrent for torrent in torrents
        if torrent['dl_limit']
    ]

    to_remove_limit = []
    for torrent in has_limit_torrents:
        progress = torrent['progress']
        up_speed = torrent['upspeed']
        if progress == 1.0:
            to_remove_limit.append(torrent)
        elif up_speed > THRESHOLD:
            to_remove_limit.append(torrent)

    if to_remove_limit:
        for torrent in to_remove_limit:
            torrent.setDownloadLimit(0)
            message = 'LIMIT -\t: `{}`'.format(torrent['name'])
            logging.warning(message)

    return to_remove_limit


def limit():
    add_limit()
    remove_limit()
