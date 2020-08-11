from tornado.escape import json_decode
from tornado.web import RequestHandler


class HomeHandler(RequestHandler):
	def get(self):
		self.render("../templates/index.html")


class KeyPressHandler(RequestHandler):
	def post(self):
		body = json_decode(self.request.body)
		keypress = body.get("key")
		print('keypress event: ' + keypress)
		self.write("received keypress event for: " + keypress)
