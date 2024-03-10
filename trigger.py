from abort import abort
from dead import clean_dead
from obsolete import cleanup
from reboot import reboot_on_stall


def check_abort():
    return abort()


def check_cleanup():
    return cleanup()


def check_dead():
    return clean_dead()


def check_reboot():
    return reboot_on_stall()
