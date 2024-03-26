# common

NOTIFY_PATH = '/usr/bin/notify'
TORRENT_DIR = '/mnt/hdd/BT'

TORRENTS_CSV = '/home/kuma/qbt/torrents.csv'

# TJU
CAT = 'TJU'
KiB = 1024
MiB = 1024 ** 2
GiB = 1024 ** 3
DAY = 24 * 60 * 60
REBOOT_INTERVAL = 1 * DAY

SEEDING_REQ = {
    """
    种子大小<=10GiB 时，B=1天（24h）
    10-20GiB 时，B=2天（48h）
    20-30GiB 时，B=3天（72h）
    30-40GiB 时，B=4天（96h）
    40-50GiB 时，B=5天（120h）
    >50GiB 时，B=7天（168h）
    """
    '<=10GiB': {
        'range_min': 0,
        'range_max': 10 * GiB,
        'required': 1 * DAY
    },
    '10-20GiB': {
        'range_min': 10 * GiB,
        'range_max': 20 * GiB,
        'required': 2 * DAY
    },
    '20-30GiB': {
        'range_min': 20 * GiB,
        'range_max': 30 * GiB,
        'required': 3 * DAY
    },
    '30-40GiB': {
        'range_min': 30 * GiB,
        'range_max': 40 * GiB,
        'required': 4 * DAY
    },
    '40-50GiB': {
        'range_min': 40 * GiB,
        'range_max': 50 * GiB,
        'required': 5 * DAY
    },
    '>50GiB': {
        'range_min': 50 * GiB,
        'range_max': 9999 * GiB,
        'required': 7 * DAY
    }
}

# abort
MAX_DONE = 0.1  # 10%
MIN_DONE = 0.01  # 1%

# cleanup
DISK_SPACE = 50 * GiB
STALL_TIME = 1 * DAY

# reboot

EXIT_QBT = 'sudo -s systemctl stop qbittorrent-nox@kuma'
REBOOT_CMD = 'sudo -s reboot'
