#!/usr/bin/env python
"""
.d88b.           8
YPwww. Yb  dP .d88 8d8b. .d88b Yb  dP   88b. Yb  dP
    d8  YbdP  8  8 8P Y8 8.dP'  YbdP    8  8  YbdP
`Y88P'   dP   `Y88 8   8 `Y88P   dP   w 88P'   dP
        dP                      dP      8     dP
"""
import time
import redis
import logging

class Frycook:
    def __init__(self, redis_srv='127.0.0.1', redis_port=6379,
            redis_db=0, redis_use_socket=False, redis_socket='/tmp/redis.sock',
            redis_ch_alerts='alerts', redis_ch_acks='acks', alert_sep='/',
            debug=False):
        # Lumberjack
        if debug:
            logging.basicConfig(level = logging.DEBUG)
        else:
            logging.basicConfig(level = logging.ERROR)

        # Redis connect
        if redis_use_socket:
            self.r = redis.StrictRedis(unix_socket_path=redis_socket, db=redis_db)
        else:
            self.r = redis.StrictRedis(host=redis_srv, port=redis_port, db=redis_db)
        self.ch_alerts = redis_ch_alerts
        self.ch_acks = redis_ch_acks
        self.alert_sep = alert_sep

    """ It seems like this method could be multithreaded, and be 500x faster, right?
    It could!
    If it weren't for python's global interpreter lock!
    """
    def order_up(self, filter): # returns filtered array of alerts
        alerts = []
        prefix = ''
        if filter['box'] != None:
            logging.debug(filter)
            prefix = filter['box']
        for key in self.r.keys(prefix + '*'):
            alerts.append(self.r.hgetall(key))
        """ TODO: Implement filtering
        if 'region' in filter:
            filter_region(alerts, filter['region'])
        if 'hostgroup' in filter:
            filter_hostgroup(alerts, filter['hostgroup'])
        if 'min_severity' in filter or 'max_severity' in filter:
            min = filter['min_severity'] if('min_severity' in filter) else 0
            max = filter['max_severity'] if('max_severity' in filter) else 5
            filter_severity(alerts, min=min, max=max)
        if 'before' in filter or 'since' in filter:
            before = filter['before'] if('before' in filter) else 2147483647
            since = filter['since'] if('since' in filter) else 0
            filter_time(alerts, before=before, since=since)
        if 'acked' in filter:
            filter_acked(alerts, acked=filter['acked'])
        if 'active' in filter:
            filter_active(alerts, active=filter['active'])
        if 'last' in filter:
            filter_last(alerts, last=filter['last'])
        """
        return alerts

    # TODO: Implement filtering.

    def filter_region(self, alerts, regions=[]):
        if len(regions) == 0:
            return

    def filter_hostgroup(self, alerts, hostgroups=[]):
        if len(hostgroup) == 0:
            return

    def filter_severity(self, alerts, min=1, max=5):
        if min == 1 and max == 5:
            return

    def filter_time(self, alerts, before=2147483647, since=0): # before=max 32 bit epoch
        if before == 2147483647 and since == 0:
            return

    def filter_acked(self, alerts, acked=0):
        if acked == 0:
            return

    def filter_active(self, alerts, active=-1):
        if active == -1:
            return

    def filter_last(self, alerts, last=0):
        if last == 0:
            return
