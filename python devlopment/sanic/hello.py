from sanic import Sanic
from sanic.response import text

app = Sanic("MyHelloWorldApp")

@app.get("/")
async def hello_world(request):
    return text("Hello, world.")
if __name__ == "__main__":
    # Sanic spins up its own production-ready server on port 8000 by default
    app.run(host="127.0.0.1", port=8000, debug=True, auto_reload=True)