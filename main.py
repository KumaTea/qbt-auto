from session import logger, scheduler
from trigger import check_abort, check_cleanup


def register():
    scheduler.add_job(check_abort, 'cron', minute='*/5', id='check_abort')
    scheduler.add_job(check_cleanup, 'cron', hour='*', id='check_cleanup')
    logger.info('Jobs registered.')


if __name__ == '__main__':
    check_abort()
    check_cleanup()
    register()
    scheduler.start()
