#!/usr/bin/env python
"""
.d88b.           8                                  
YPwww. Yb  dP .d88 8d8b. .d88b Yb  dP   88b. Yb  dP 
    d8  YbdP  8  8 8P Y8 8.dP'  YbdP    8  8  YbdP  
`Y88P'   dP   `Y88 8   8 `Y88P   dP   w 88P'   dP   
        dP                      dP      8     dP    
"""
import logging
import ConfigParser
from Sydney import frycook
from Sydney import waitress

# Lumberjack
logging.basicConfig(level=logging.DEBUG)

# Config
conf = ConfigParser.SafeConfigParser()
conf.read('./sydney.conf')
chef = frycook.Frycook(
        redis_use_socket=conf.get('redis', 'use_socket'),
        redis_socket=conf.get('redis', 'socket'))
waitress = waitress.Waitress(chef, bind=conf.get('waitress', 'bind'),
        port=conf.get('waitress', 'port'),
        api_prefix=conf.get('waitress', 'api_prefix'),
        debug=True)
        #debug=conf.get('waitress', 'debug'))
