import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Welcome to WSS')


class HealthCheckHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("OK")


class EchoWebSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket opened")
        self.write_message("Hello World")

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print("WebSocket closed")

    def check_origin(self, origin):
        return True


HANDLERS = [
    (r"/", MainHandler),
    (r"/echo", EchoWebSocket),
    (r"/_ah/health", HealthCheckHandler),
    (r"/_ah/start", HealthCheckHandler)
]

app = tornado.web.Application(HANDLERS)


def main():
    app.listen(8080)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
