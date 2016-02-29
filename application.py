#!/usr/bin/env python
# coding=utf-8

from url import url

import tornado.web
import os
import pymongo
from tornado.options import define, options
define("mongo_url", default="localhost", help="location of mongodb", type=str)
define("mongo_port", default=27017, help="port mongodb is listening on", type=int)
define("mongo_dbname", default="sampledb", help="name of the database", type=str)

settings = {'template_path': os.path.join(os.path.dirname(__file__), "templates"),
            'static_path': os.path.join(os.path.dirname(__file__), "statics"),
            'debug': True,
            "cookie_secret": "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
            "xsrf_cookies": True,
            "login_url": "/login"
            }

application = tornado.web.Application(
    **settings,
    handlers=url,
    conn = pymongo.MongoClient(options.mongo_url, options.mongo_port)
)
