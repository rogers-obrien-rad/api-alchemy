import requests
import argparse

def get_image(sub_id=None):

    url = "https://api.thecatapi.com/v1/images/search"

    if sub_id:
        params = {"sub_id": sub_id}
    else:
        params = {}

    headers = {
        'x-api-key': 'live_NMNC1lcbODoViW3HxtYkiIstzdDd8wN2e8tlHLM6QyDGSKTA1NUGGdqEGP7UOoBm'
    }

    response = requests.request("GET", url, headers=headers, params=params)

    print(response.json()[0]["url"])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch a cat image. Optionally provide a sub_id.")
    parser.add_argument('--sub_id', type=str, help="An optional sub_id string.")
    args = parser.parse_args()
    
    get_image(args.sub_id)