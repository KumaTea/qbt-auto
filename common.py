import os
import csv
from config import TORRENTS_CSV
from qbittorrentapi.torrents import TorrentDictionary  # , TorrentInfoList


def get_torrents_by_category(torrents: list[TorrentDictionary], category: str = None) -> list[TorrentDictionary]:
    """
    Get torrents by category
    if category is empty, return all torrents without category
    """
    filtered = []
    if category:
        for torrent in torrents:
            if torrent['category'] == category:
                filtered.append(torrent)
    else:  # category is None
        for torrent in torrents:
            if not torrent['category']:
                filtered.append(torrent)
    return filtered


def get_torrents_by_tag(torrents: list[TorrentDictionary], tag: str = None) -> list[TorrentDictionary]:
    """
    Get torrents by tag
    if tag is empty, return all torrents without tag
    """
    filtered = []
    if tag:
        for torrent in torrents:
            if tag in torrent['tags']:
                filtered.append(torrent)
    else:  # tag is None
        for torrent in torrents:
            if not torrent['tags']:
                filtered.append(torrent)
    return filtered


def write_torrent_info(torrent: TorrentDictionary):
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
