from abort import abort
from limit import limit
from dead import clean_dead
from obsolete import cleanup
from removed import del_removed
from reboot import reboot_on_stall


def check_abort():
    return abort()


def check_removed():
    return del_removed()


def check_limit():
    return limit()


def check_cleanup():
    return cleanup()


def check_dead():
    return clean_dead()


def check_reboot():
    return reboot_on_stall()
