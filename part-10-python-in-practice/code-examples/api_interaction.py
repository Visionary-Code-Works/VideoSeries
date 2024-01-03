# api_interaction.py

import requests
import json

def get_data_from_api(url):
    """ Send a GET request to the specified API and return the JSON response """
    try:
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            return response.json()  # Parse and return the JSON data
        else:
            return f"Error: {response.status_code}"
    except requests.RequestException as e:
        return f"Error: {e}"

def main():
    # Example API URL (You can replace this with any API URL you wish to interact with)
    api_url = 'https://jsonplaceholder.typicode.com/posts'

    # Get data from API
    data = get_data_from_api(api_url)

    # If the data is a list (as expected from this API), print the first few items
    if isinstance(data, list):
        print(json.dumps(data[:5], indent=2))  # Print the first 5 posts
    else:
        print(data)

if __name__ == '__main__':
    main()
