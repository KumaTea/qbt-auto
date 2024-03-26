import logging
import configparser
import qbittorrentapi
from apscheduler.schedulers.blocking import BlockingScheduler


logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.WARNING,
    datefmt='%Y-%m-%d %H:%M:%S')

config = configparser.ConfigParser()
config.read('config.ini')
qbt = qbittorrentapi.Client(
    host=config['qbt']['host'],
    port=config['qbt']['port'],
    username=config['qbt']['username'],
    password=config['qbt']['password']
)

scheduler = BlockingScheduler()
