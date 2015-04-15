#!/usr/bin/env python
"""
.d88b.           8
YPwww. Yb  dP .d88 8d8b. .d88b Yb  dP   88b. Yb  dP
    d8  YbdP  8  8 8P Y8 8.dP'  YbdP    8  8  YbdP
`Y88P'   dP   `Y88 8   8 `Y88P   dP   w 88P'   dP
        dP                      dP      8     dP
"""
import logging
from flask import Flask
from flask.ext import restful
from flask.ext.restful import Resource, Api, reqparse

resources = dict()
chef = ''

class Waitress:
    def __init__(self, frycook, bind='127.0.0.1', port=5000,
            api_prefix='/api/v0.1', debug=False):
        if debug:
            logging.basicConfig(level = logging.DEBUG)
        else:
            logging.basicConfig(level = logging.ERROR)
        self.frycook = frycook
        global chef
        chef = frycook
        self.app = Flask(__name__)
        self.api = restful.Api(self.app)
        self.prefix = api_prefix
        logging.debug(resources)
        for res in resources:
            self.api.add_resource(resources[res], api_prefix + res)
        self.app.run(debug=debug)

# Flask Routing
class Slash(Resource):
    def get(self):
        logging.debug(self.__bases__)
        return {'battlecruiser': 'operational'}
resources['/'] = Slash # Add us to the default load list with endpoint

class Alert(Resource):
    def get(self):
        args = problem_parser.parse_args()
        return chef.order_up(args)
resources['/alerts'] = Alert

class Ack(Resource):
    def get(self):
        pass # TODO define


""" Flask Req Parsers
"""
problem_parser = reqparse.RequestParser()
problem_parser.add_argument('hostgroup', type=str, action='append')
problem_parser.add_argument('box', type=str, action='append')
problem_parser.add_argument('active', type=int)
problem_parser.add_argument('since', type=int)
problem_parser.add_argument('before', type=int)
problem_parser.add_argument('limit', type=int)
problem_parser.add_argument('last',  type=int)
problem_parser.add_argument('region', type=int)
problem_parser.add_argument('min_severity', type=int)
problem_parser.add_argument('max_severity', type=int)
problem_parser.add_argument('acked', type=int)
