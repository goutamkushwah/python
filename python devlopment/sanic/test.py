from sanic import Sanic
from sanic.response import json
app = Sanic("MyHelloWorldApp")
@app.route("/")
async def hello_world(request):
    return json({"message": "Hello, world."})
if __name__ == "__main__":  
    app.run(host="0.0.0.0", port=8000)