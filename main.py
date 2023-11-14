from session import logger, scheduler
from trigger import check_abort, check_cleanup, check_dead


def register():
    scheduler.add_job(check_abort, 'cron', minute='*', id='check_abort')
    scheduler.add_job(check_cleanup, 'cron', hour='*', id='check_cleanup')
    scheduler.add_job(check_dead, 'cron', day='*', id='check_dead')
    logger.info('Jobs registered.')


if __name__ == '__main__':
    check_abort()
    check_cleanup()
    check_dead()
    register()
    scheduler.start()
