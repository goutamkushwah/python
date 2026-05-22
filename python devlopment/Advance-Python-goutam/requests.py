import requests

# 1. GET: Retrieve data
# We'll fetch the latest public events from GitHub
print("--- GET Request ---")
r_get = requests.get('https://api.github.com/events')
print(f"Status: {r_get.status_code}")
# Print the first event's type as an example
if r_get.status_code == 200:
    print(f"First Event Type: {r_get.json()[0]['type']}\n")

# 2. POST: Create data
# httpbin.org is a great service for testing requests
print("--- POST Request ---")
payload = {'user': 'gemini', 'action': 'testing'}
r_post = requests.post('https://httpbin.org/post', data=payload)
print(f"Status: {r_post.status_code}")
print(f"Server received: {r_post.json()['form']}\n")

# 3. PUT: Update data
print("--- PUT Request ---")
r_put = requests.put('https://httpbin.org/put', data={'key': 'updated_value'})
print(f"Status: {r_put.status_code}")
print(f"Updated data: {r_put.json()['form']}\n")

# 4. DELETE: Remove data
print("--- DELETE Request ---")
r_delete = requests.delete('https://httpbin.org/delete')
print(f"Status: {r_delete.status_code}\n")

# 5. HEAD: Get headers only (no body)
print("--- HEAD Request ---")
r_head = requests.head('https://httpbin.org/get')
print(f"Content-Type: {r_head.headers.get('Content-Type')}")
print(f"Response body length: {len(r_head.text)} (Should be 0)\n")

# 6. OPTIONS: Check allowed methods
print("--- OPTIONS Request ---")
r_options = requests.options('https://httpbin.org/get')
print(f"Allowed Methods: {r_options.headers.get('Allow')}")
