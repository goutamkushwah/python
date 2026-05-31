# main.py
from sanic import Sanic
from sanic import response
from sanic.log import logger
from controller import my_bp

# Initialize the Sanic application
app = Sanic("My_First_Sanic_App")

# Registering the blueprint defined in controller.py
app.blueprint(my_bp)


# Webapp path defined using 'route' decorator (Default is GET)
@app.route("/")
async def run(request):
    return response.text("Hello World !")


# POST route with robust JSON exception handling
@app.route("/post", methods=['POST'])
async def on_post(request):
    try:
        # request.json automatically parses incoming JSON data
        return response.json({"content": request.json})
    except Exception as ex:
        import traceback
        logger.error(f"JSON Parsing Error: {traceback.format_exc()}")
        
        # CRITICAL FIX: Always return a response object, even on failure
        return response.json(
            {"error": "Bad Request", "message": "Invalid or missing JSON body."}, 
            status=400
        )


if __name__ == "__main__":
    # Runs the server on http://localhost:8000
    app.run(host="0.0.0.0", port=8000, debug=True)