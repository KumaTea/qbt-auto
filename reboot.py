"""
Check torrents status
If all torrents are inactive, reboot the system
"""


import time
import subprocess
from session import logging, tor
from config import REBOOT_INTERVAL


def get_uptime() -> float:
    # return uptime in seconds

    # approach 1
    # ok for lxc
    with open('/proc/uptime', 'r') as f:
        uptime = float(f.readline().split()[0])

    # approach 2
    # uptime = time.time() - psutil.boot_time()

    # approach 3
    # fails on lxc
    # uptime = time.monotonic()

    # approach 4
    # fails on lxc
    # uptime = time.clock_gettime(time.CLOCK_BOOTTIME)
    return uptime


def reboot_on_stall():
    uptime = get_uptime()
    if uptime < REBOOT_INTERVAL:
        return logging.debug('Uptime {}s is less than threshold {}s'.format(int(uptime), REBOOT_INTERVAL))

    torrents = tor.get()
    states = [torrent['state'] for torrent in torrents]
    states = list(set(states))

    if all('stalled' in state for state in states):
        logging.warning('All torrents are stalled. Rebooting...')
        subprocess.run('sudo -s systemctl stop qbittorrent-nox@kuma', shell=True)
        time.sleep(2)
        return subprocess.run('sudo -s reboot', shell=True)
