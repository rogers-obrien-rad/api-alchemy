import requests

def favorite_image():

    url = "https://api.thecatapi.com/v1/favourites"

    headers = {
        'x-api-key': 'live_NMNC1lcbODoViW3HxtYkiIstzdDd8wN2e8tlHLM6QyDGSKTA1NUGGdqEGP7UOoBm',
    }

    data = {
        'image_id': 'h-bMdWYmd'
    }

    response = requests.post(url, headers=headers, json=data)

    print(response.text)

if __name__ == "__main__":
    favorite_image()
