import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
import httplib2
import os


NETWORK_INTERFACE_METADATA_URL = "http://metadata.google.internal/computeMetadata/v1/instance/network-interfaces/0/" \
                                 "access-configs/0/external-ip"


def get_host_name():
    if os.environ.get('GAE_PARTITION', 'prod') != 'dev':
        http = httplib2.Http()
        response, content = http.request(NETWORK_INTERFACE_METADATA_URL,
                                         headers={'Metadata-Flavor': 'Google'})
        return content
    else:
        return 'localhost'


def get_websocket_url():
    return "ws://%s:8080/echo" % get_host_name()


class InfoHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(get_websocket_url())


class HealthCheckHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("ok")


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
    (r"/echo", EchoWebSocket),
    (r"/info", InfoHandler),
    (r"/_ah/health", HealthCheckHandler),
    (r"/_ah/start", HealthCheckHandler)
]

app = tornado.web.Application(HANDLERS)


def main():
    app.listen(8080)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
