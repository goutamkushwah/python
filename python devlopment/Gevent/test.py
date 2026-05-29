from gevent import monkey
monkey.patch_all()  # Crucial: Must be line #1 before importing other modules

from gevent.pywsgi import WSGIServer
import random
import time
import web

# FIX: Disable web.py's internal debug/threading loops 
# This allows gevent's WSGIServer to handle the concurrency natively.
web.config.debug = False

urls = (
    "/", "index",
    "/long", "long_polling",
    "/verylong", "very_long_polling"
)

class index(object):
    def GET(self):
        return "<h1>Default context route</h1>"

class long_polling(object):
    def GET(self):
        waittime = random.randint(1, 5)
        time.sleep(waittime)  # Gevent intercepts this and yields control
        return f"<h1>Long polling: {waittime}</h1>"

class very_long_polling(object):
    def GET(self):
        waittime = random.randint(10, 20)
        time.sleep(waittime)  # Gevent intercepts this and yields control
        return f"<h1>Very Long polling: {waittime}</h1>"        

# Extract the WSGI function
app = web.application(urls, globals())
application = app.wsgifunc()

if __name__ == "__main__":
    print("Serving on port 8099...")
    # WSGIServer spawns a ultra-lightweight greenlet for every incoming connection
    server = WSGIServer(('127.0.0.1', 8099), application)
    server.serve_forever()