"""
Delete torrents that have seeded long enough
and not active
"""


import subprocess
from config import *
from session import logger
from common import get_torrents, get_torrents_by_category, get_torrents_by_tag, write_torrent_info


def meet_req(torrent):
    for key, value in SEEDING_REQ.items():
        if value['range_min'] <= torrent['size'] < value['range_max']:
            if torrent['seeding_time'] > value['required']:
                return True
    return False


def cleanup():
    torrents = get_torrents_by_tag(
        get_torrents_by_category(
            get_torrents(),
            category=CAT
        ),
        tag=''
    )

    # 1. finished (torrent['progress'] == 1)
    # 2. not active (torrent['upspeed'] == 0)
    # 3. seeded long enough (torrent['seeding_time'] exceeds SEEDING_REQ)

    to_cleanup = []
    for torrent in torrents:
        if torrent['progress'] == 1:
            if torrent['upspeed'] == 0:
                if meet_req(torrent):
                    to_cleanup.append(torrent)

    if to_cleanup:
        for torrent in to_cleanup:
            if not torrent['upspeed']:
                subprocess.run(REANNOUNCE_TORRENT.format(HASH=torrent['hash']).split())
                write_torrent_info(torrent)
                subprocess.run(DELETE_TORRENT.format(HASH=torrent['hash']).split())
                message = 'Torrent `{}` cleaned up'.format(torrent['name'])
                logger.warning(message)
                # subprocess.run(NOTIFY.format(MESSAGE=message).split())
                subprocess.run([NOTIFY_PATH, message])

    return to_cleanup
