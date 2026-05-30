from aiohttp import web
import json

async def new_user(request):
    try:
        ## happy path where name is set
        user = request.query['name']
        ## Process our new user
        print("Creating new user with name: ", user)

        response_obj = { 'status' : 'success' }
        ## return a success json response with status code 200 i.e. 'OK'
        return web.Response(text=json.dumps(response_obj), status=200)
    except Exception as e:
        ## Bad path where name is not set
        response_obj = { 'status' : 'failed', 'reason': str(e) }
        ## return failed with a status code of 500 i.e. 'Server Error'
        return web.Response(text=json.dumps(response_obj), status=500)

# 1. Create the application instance
app = web.Application()

# 2. Bind your function to the '/register' route
app.router.add_get('/register', new_user)

# 3. Execution block to start the server
if __name__ == "__main__":
    print("Starting server on http://127.0.0.1:8085")
    web.run_app(app, host="127.0.0.1", port=8085)