"""
Clean up dead torrents
"""


import time
import subprocess
from config import *
from session import logger
from common import get_torrents, get_torrents_by_category, get_torrents_by_tag, write_torrent_info


def meet_dead_req(torrent):
    if torrent['progress'] < 0.01 and torrent['state'] == 'stalledDL':
        if time.time() - torrent['added_on'] > STALL_TIME:
            return True
    return False


def clean_dead():
    torrents = get_torrents_by_tag(
        get_torrents_by_category(
            get_torrents(),
            category=CAT
        ),
        tag=''
    )

    to_cleanup = []
    for torrent in torrents:
        if meet_dead_req(torrent):
            to_cleanup.append(torrent)

    if to_cleanup:
        for torrent in to_cleanup:
            write_torrent_info(torrent)
            subprocess.run(DELETE_TORRENT.format(HASH=torrent['hash']).split())
            message = 'Torrent `{}` cleaned up'.format(torrent['name'])
            logger.warning(message)

    return to_cleanup
