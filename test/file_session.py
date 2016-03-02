#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
import tornado.httpserver
import tornado.ioloop
from torndsession.sessionhandler import SessionBaseHandler


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r'/del', DeleteHandler),
        ]
        settings = dict(
            debug = True,
        )
        session_settings = dict(
            driver = "file",
            driver_settings = dict(
                host = "sessions",
            ),
            force_persistence = True,
        )
        settings.update(session=session_settings)
        tornado.web.Application.__init__(self, handlers, **settings)


class MainHandler(SessionBaseHandler):
    def get(self):
        self.write("File Session Example:<br/>")
        # print self.session.keys()
        if "sv" in self.session:
            self.write('sv in session<br/>')
            sv = self.session["sv"]
        else:
            self.write('sv not in session<br/>')
            sv = 0
        if sv == None:
            sv = 0
        else:
            sv = int(sv)+1
        self.write('Current Session Value:%d' % sv)
        # self.write(self.session.keys())
        self.session["sv"] = sv

class DeleteHandler(SessionBaseHandler):
    def get(self):
        '''
        Please don't do this in production environments.
        '''
        self.write("Memory Session Object Demo:")
        if "sv" in self.session:
            current_value = self.session["sv"]
            self.write("current sv value is %s, and system will delete this value.<br/>" % self.session["sv"])
            self.session.delete("sv")
            if "sv" not in self.session:
                self.write("current sv value is empty")
        else:
            self.write("Session data not found")

def main():
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    print("0000")
    main()