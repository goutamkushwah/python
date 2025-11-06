import requests

# URL to fetch data from
url = "https://api.github.com"

# Sending a GET request to the URL
response = requests.get(url)

# Checking the status
if response.status_code == 200:
    print("Request Successful!")
    print("Data received from GitHub API:")
    print(response.json())  # print JSON data
else:
    print("Failed to retrieve data. Status code:", response.status_code)
