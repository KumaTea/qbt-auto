"""
Abort torrents that downloaded under 10%
and has a share ratio lower than finish percentage
"""

import subprocess
from config import *
from session import logger
from common import get_torrents, get_torrents_by_category, get_torrents_by_tag


def abort():
    torrents = get_torrents_by_tag(
        get_torrents_by_category(
            get_torrents(),
            category=CAT
        ),
        tag=''
    )

    to_abort = []
    for torrent in torrents:
        if MIN_DONE < torrent['progress'] < MAX_DONE:
            if torrent['ratio'] < MAX_DONE:
                to_abort.append(torrent)

    if to_abort:
        for torrent in to_abort:
            subprocess.run(DELETE_TORRENT.format(HASH=torrent['hash']).split())
            message = 'Torrent `{}` aborted'.format(torrent['name'])
            logger.warning(message)
            # subprocess.run(NOTIFY.format(MESSAGE=message).split())
            subprocess.run([NOTIFY_PATH, message])

    return to_abort
