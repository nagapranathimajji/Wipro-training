import requests
url= 'https://jsonplaceholder.typicode.com/posts'
data={
    "title": "Hi students",
    "body": "This is a post request",
    "userId": 1
}
response = requests.post(url, json=data)
print("Status Code:", response.status_code)  # Print the status code of the response
print("Response JSON:", response.json())  # Print the JSON content of the response