import logging
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from common import *


logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')


class TorrentStore:
    def __init__(self):
        self.torrents: list[dict] = []
        self.last_saved: datetime = datetime.now()
        self.refresh()

    def refresh(self):
        self.torrents = get_torrents()

    def get(self):
        if (datetime.now() - self.last_saved).seconds > 30:
            self.refresh()
        return self.torrents


scheduler = BlockingScheduler()
tor = TorrentStore()
