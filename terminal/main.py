import sys, os
# sys.path.append(os.path.dirname(__file__))


import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.options
import tornado.wsgi
from tornado.options import options, parse_command_line
from terminal import config, ioloop

import django.core.handlers.wsgi

from terminal.handlers import *

wsgi_app = tornado.wsgi.WSGIContainer(django.core.handlers.wsgi.WSGIHandler())

settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
)

handlers = [
    (r"/t/", IndexHandler),
    (r"/t/login", IndexHandler),
    (r"/t/ws", WSHandler),
    ('.*', tornado.web.FallbackHandler, dict(fallback=wsgi_app)),
]


class Application(tornado.web.Application):
    def __init__(self):
        super(Application, self).__init__(handlers, **settings)


def welcome(port):
    print('''
Welcome to the webssh!
                __              __
 _      _____  / /_  __________/ /_
| | /| / / _ \/ __ \/ ___/ ___/ __ \\
| |/ |/ /  __/ /_/ (__  |__  ) / / /
|__/|__/\___/_.___/____/____/_/ /_/

Now start~
Please visit the localhost:%s from the explorer~
    ''' % port)


def main():
    parse_command_line()

    config.init_config()
    options.parse_config_file("webssh.conf")

    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    ioloop.IOLoop.instance().start()
    welcome(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MiracleOps.settings")
    if django.VERSION[1] > 5:
        django.setup()
    main()
