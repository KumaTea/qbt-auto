import logging
from apscheduler.schedulers.blocking import BlockingScheduler


logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

logger = logging.getLogger(__name__)
scheduler = BlockingScheduler()
