# requests_web_requests.py
import requests

# Making a GET Request
def make_get_request(url):
    response = requests.get(url)
    print("GET Request to", url)
    print("Status Code:", response.status_code)
    print("Response Content:\n", response.text)

# Making a POST Request
def make_post_request(url, data):
    response = requests.post(url, data=data)
    print("\nPOST Request to", url)
    print("Status Code:", response.status_code)
    print("Response Content:\n", response.text)

# Example usage
example_url = 'https://httpbin.org/get'
make_get_request(example_url)

example_post_url = 'https://httpbin.org/post'
post_data = {'key': 'value'}
make_post_request(example_post_url, post_data)
