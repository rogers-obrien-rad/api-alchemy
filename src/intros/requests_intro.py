# Introduction to the 'requests' Library in Python

# --- Package Import ---
# The 'requests' library simplifies making requests to web services and handling responses.
import requests

# --- Base Components of an HTTP Request ---
# - URL: The endpoint where the request is made.
# - Headers: Metadata sent with the request.
# - Parameters: Data appended to the URL for GET requests.
# - Body/Data: Data sent with the request (common for POST, PUT requests).

# --- Making a GET Request ---
# The GET method is used to retrieve data from a server.

url = 'https://jsonplaceholder.typicode.com/posts/1'
headers = {}  # Empty headers dictionary
params = {}  # Empty parameters dictionary

response_get = requests.get(url, headers=headers, params=params)

# Checking if the request was successful
if response_get.status_code == 200:
    print("GET request was successful!")
else:
    print(f"Failed with status code: {response_get.status_code}")

# --- Response Content ---
# The 'text' attribute provides the response content as a string.
print("\nResponse Content:")
print(response_get.text)

# --- Parsing JSON Responses ---
# If the response is in JSON format, we can parse it into a Python dictionary.
data = response_get.json()
print("\nParsed JSON:")
print(data)

# Accessing specific data from the parsed JSON
print(f"Title of the post: {data['title']}")

# --- HTTP Headers ---
# Headers provide meta-information about the response or request.
print("\nResponse Headers:")
print(response_get.headers)

# Accessing a specific header value
content_type = response_get.headers['Content-Type']
print(f"Content Type: {content_type}")

# --- Making a POST Request ---
# 'POST' is used to send data to a server to create a resource.
url = 'https://jsonplaceholder.typicode.com/posts'
headers = {
    'Content-type': 'application/json; charset=UTF-8'  # Header for sending JSON data
}
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

response_post = requests.post(url, headers=headers, json=data)

# Checking and displaying the result of the POST request
if response_post.status_code == 201:
    print("\nPOST request was successful!")
    print(response_post.json())
else:
    print(f"POST request failed with status code: {response_post.status_code}")

# --- Making a PUT Request ---
# The PUT method is used to update a resource on a server.

url = 'https://jsonplaceholder.typicode.com/posts/1'
headers = {
    'Content-type': 'application/json; charset=UTF-8'
}
data = {
    'id': 1,
    'title': 'Updated title',
    'body': 'Updated body',
    'userId': 1
}

response = requests.put(url, headers=headers, json=data)

print("\nPUT Request Response:")
print(response.json())

# --- Making a DELETE Request ---
# The DELETE method is used to delete a resource on a server.

url = 'https://jsonplaceholder.typicode.com/posts/1'
headers = {}  # Empty headers dictionary

response = requests.delete(url, headers=headers)

print("\nDELETE Request Response:")
print(response.status_code)  # For DELETE, a successful call typically returns a 200 or 204 status code.