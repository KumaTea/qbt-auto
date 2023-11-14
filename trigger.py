import shutil
from config import *
from abort import abort
from session import logger
from dead import clean_dead
from obsolete import cleanup


def check_abort():
    return abort()


def check_cleanup():
    total, used, free = shutil.disk_usage(TORRENT_DIR)
    if free < DISK_SPACE:
        return cleanup()
    else:
        return logger.debug('Disk space is enough: {} GiB'.format(free / GiB))


def check_dead():
    return clean_dead()
