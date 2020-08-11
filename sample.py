from tornado.ioloop import IOLoop
from tornado.web import Application

from handlers import *
from settings import *

TORNADO_ROUTES = [
	(r'/?', HomeHandler),
	(r'/api/keypress', KeyPressHandler)
]

application = Application(TORNADO_ROUTES, **TORNADO_SETTINGS)

if __name__ == '__main__':
	application.listen(8080)
	IOLoop.instance().start()
