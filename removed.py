"""
Abort torrents that downloaded under 10%
and has a share ratio lower than finish percentage
"""

from config import CAT
from session import logging, qbt
from common import get_torrents_by_category, get_torrents_by_tag, write_torrent_info


def del_removed():
    torrents = get_torrents_by_tag(
        get_torrents_by_category(
            qbt.torrents.info.all(),
            category=CAT
        ),
        tag=None
    )

    to_del = []
    for torrent in torrents:
        trackers = qbt.torrents_trackers(torrent['hash'])
        for tracker in trackers:
            if tracker['msg'] == '006-种子尚未上传或者已经被删除':
                to_del.append(torrent)
                break

    if to_del:
        for torrent in to_del:
            write_torrent_info(torrent)
            torrent.delete(delete_files=True)
            message = 'ABORT\t: `{}`'.format(torrent['name'])
            logging.warning(message)

    return del_removed
