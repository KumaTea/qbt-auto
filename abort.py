"""
Abort torrents that downloaded under 10%
and has a share ratio lower than finish percentage
"""

import time
from session import logging, qbt
from config import CAT, MIN_DONE, MAX_DONE
from common import get_torrents_by_category, get_torrents_by_tag, write_torrent_info


def abort():
    torrents = get_torrents_by_tag(
        get_torrents_by_category(
            qbt.torrents.info.all(),
            category=CAT
        ),
        tag=None
    )

    to_abort = []
    for torrent in torrents:
        # if 'checking' not in torrent['state'] and
        if torrent['ratio'] < MAX_DONE:
            if MIN_DONE < torrent['progress'] < MAX_DONE:
                to_abort.append(torrent)
            elif MIN_DONE < torrent['progress'] < 2 * MAX_DONE and time.time() - torrent['added_on'] < 300:
                # <20% but less than 5 minutes
                to_abort.append(torrent)

    if to_abort:
        for torrent in to_abort:
            write_torrent_info(torrent)
            # subprocess.run(DELETE_TORRENT.format(HASH=torrent['hash']).split())
            torrent.delete(delete_files=True)
            message = 'ABORT\t: `{}`'.format(torrent['name'])
            logging.warning(message)
            # subprocess.run(NOTIFY.format(MESSAGE=message).split())
            # subprocess.run([NOTIFY_PATH, message])

    return to_abort
