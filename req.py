import requests
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
print("Status Code:", response.status_code)  # Print the status code of the responsewhich python
print("Response JSON:", response.json())  # Print the JSON content of the response
