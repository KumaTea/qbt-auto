"""
Abort torrents that downloaded under 10%
and has a share ratio lower than finish percentage
"""

import subprocess
from config import *
from time import time
from session import logger
from common import get_torrents, get_torrents_by_category, get_torrents_by_tag, write_torrent_info


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
        if torrent['ratio'] < MAX_DONE:
            if MIN_DONE < torrent['progress'] < MAX_DONE:
                to_abort.append(torrent)
            elif MIN_DONE < torrent['progress'] < 2 * MAX_DONE and time() - torrent['added_on'] < 300:
                # <20% but less than 5 minutes
                to_abort.append(torrent)

    if to_abort:
        for torrent in to_abort:
            write_torrent_info(torrent)
            subprocess.run(DELETE_TORRENT.format(HASH=torrent['hash']).split())
            message = 'Torrent `{}` aborted'.format(torrent['name'])
            logger.warning(message)
            # subprocess.run(NOTIFY.format(MESSAGE=message).split())
            # subprocess.run([NOTIFY_PATH, message])

    return to_abort
