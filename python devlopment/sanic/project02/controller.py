# controller.py
from sanic import Blueprint
from sanic import response

# Create the blueprint instance
my_bp = Blueprint("my_blueprint", url_prefix="/api")

@my_bp.route("/hello")
async def bp_hello(request):
    """
    This route will be accessible at http://localhost:8000/api/hello
    """
    return response.json({"message": "Hello from the Blueprint!"})