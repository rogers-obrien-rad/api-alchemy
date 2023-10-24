import requests

def post_image():

    url = "https://api.thecatapi.com/v1/images/upload"

    payload = {
        'sub_id': 'the_chicken_nugget'
    }
    
    # Create a tuple for the file: (filename, file_object, content_type)
    files = {
        "file": ('chicken_nugget.png', open("../../images/chicken_nugget.png", 'rb'), 'image/png')
    }

    headers = {
        'x-api-key': 'live_NMNC1lcbODoViW3HxtYkiIstzdDd8wN2e8tlHLM6QyDGSKTA1NUGGdqEGP7UOoBm',
    }

    response = requests.post(url, headers=headers, data=payload, files=files)

    print(response.text)

if __name__ == "__main__":
    post_image()
