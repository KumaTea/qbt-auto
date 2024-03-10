from session import logging, scheduler
from trigger import check_abort, check_cleanup, check_dead, check_reboot


def register():
    scheduler.add_job(check_abort,   'cron',                    minute='*',  id='check_abort')
    scheduler.add_job(check_cleanup, 'cron',          hour='*', minute='15', id='check_cleanup')
    scheduler.add_job(check_dead,    'cron', day='*',                        id='check_dead')
    scheduler.add_job(check_reboot,  'cron',          hour='*', minute='30', id='check_reboot')
    logging.info('Jobs registered.')


if __name__ == '__main__':
    check_abort()
    check_cleanup()
    check_dead()
    register()
    scheduler.start()
