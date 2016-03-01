#!/usr/bin/env python
# coding=utf-8

import tornado.web
import pymongo
import json
from methods import db


#TODO 首页请求
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        # self.write(sample_data);
        self.render("index.html")

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        self.write(username)