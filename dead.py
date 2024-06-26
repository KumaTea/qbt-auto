"""
Clean up dead torrents
"""


import time
from session import logging, qbt
from config import CAT, STALL_TIME
from common import get_torrents_by_category, get_torrents_by_tag, write_torrent_info


def meet_dead_req(torrent):
    if torrent['state'] == 'stalledDL':
        if all([
            torrent['progress'] < 0.01,
            time.time() - torrent['added_on'] > STALL_TIME
        ]):
            return True
        elif all([
            torrent['progress'] < 0.1,
            time.time() - torrent['added_on'] > STALL_TIME * 2
        ]):
            return True
    return False


def clean_dead():
    torrents = get_torrents_by_tag(
        get_torrents_by_category(
            qbt.torrents.info.all(),
            category=CAT
        ),
        tag=None
    )

    to_cleanup = []
    for torrent in torrents:
        if meet_dead_req(torrent):
            to_cleanup.append(torrent)

    if to_cleanup:
        for torrent in to_cleanup:
            write_torrent_info(torrent)
            # subprocess.run(DELETE_TORRENT.format(HASH=torrent['hash']).split())
            torrent.delete(delete_files=True)
            message = 'DEAD\t: `{}`'.format(torrent['name'])
            logging.warning(message)

    return to_cleanup
