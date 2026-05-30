# importing the main event loop
import tornado.ioloop

# for HTTP requesthandlers ( to map the requests to request handlers)
import tornado.web

class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello, Tornado 🌪️!')

class PostHandler (tornado.web.RequestHandler):
    def get(self):
        self.write("<h1>This is Post 1 ✍️</h1>")

class HomeHandler (tornado.web.RequestHandler):
    def get(self):
        self.write("<h1>Welcome to Home Page 🏠</h1>")

class WeatherHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<h1>Welcome to Weather Page 🌤️</h1>")

class IntroHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<h1>Welcome to Intro Page 📚</h1>")
        self.write("")

def make_app():
    return tornado.web.Application([
        (r"/", HelloHandler),
        (r"/post", PostHandler),
        (r"/home", HomeHandler),
        (r"/weather", WeatherHandler),
        (r"/intro", IntroHandler),
    ], 
    debug = True,
    autoreload = True)



if __name__ == "__main__":
    app = make_app()
    port = 8888
    app.listen(port)
print("Server is running at http://localhost:8888/")    # to start ther server on the current thread
tornado.ioloop.IOLoop.current().start()


