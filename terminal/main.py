from tornado import ioloop, web, httpserver
from tornado.options import options
import os, sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(BASE_DIR))
print(sys.path)

import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'MiracleOps.settings'  # 设置项目的配置文件
django.setup()



from terminal.handlers import *
from terminal.config import init_config
from terminal.ioloop import IOLoop


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


settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
)

handlers = [
    (r"/", IndexHandler),
    (r"/login", IndexHandler),
    (r"/ws", WSHandler)
]


class Application(web.Application):
    def __init__(self):
        super(Application, self).__init__(handlers, **settings)


def main():
    init_config()
    options.parse_config_file(os.path.join(BASE_DIR, "webssh.conf"))

    http_server = httpserver.HTTPServer(Application())
    http_server.listen(options.port, address="0.0.0.0")
    IOLoop.instance().start()
    welcome(options.port)
    ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
