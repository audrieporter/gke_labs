# import torndado library for Python
import tornado.ioloop  
import tornado.web     

# create handler, which responds to requests. Print object.
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world!\n")
        print(self.request)

# create webserver and registers handler to respond to URL (forward slashes)
def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    # main part of app. call fn that creates server
    app = make_app()
    #make it listen on port 8888
    app.listen(8888)
    #start ioloop so server will listen for requests
    tornado.ioloop.IOLoop.current().start()