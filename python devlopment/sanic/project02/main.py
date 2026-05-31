# main.py
from sanic import Sanic
from sanic import response
from sanic.log import logger
from controller import my_bp

# App setup (No spaces in the name!)
app = Sanic("My_First_Sanic_App")

# Registering blueprint
app.blueprint(my_bp)

# Static file serving
app.static('/flowers.jpg', './flowers.jpg')


# FIX: Route updated to properly read and render 'index.html'
@app.route("/")
async def run(request):
    # response.file handles reading the HTML file asynchronously
    return await response.file("./index.html")


# POST route with JSON exception handling
@app.route("/post", methods=['POST'])
async def on_post(request):
    try:
        return response.json({"content": request.json})
    except Exception as ex:
        import traceback
        logger.error(f"JSON Parsing Error: {traceback.format_exc()}")
        return response.json(
            {"error": "Bad Request", "message": "Invalid or missing JSON body."}, 
            status=400
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)