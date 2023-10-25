import requests

# -- Edit this function -- #
def get_image():
    """
    Gets a random cat image

    Link to Documentation: https://documenter.getpostman.com/view/5578104/RWgqUxxh#997f5b37-79cc-49a4-8c11-ddf24b72a4d9
    """

    # Define the full URL
    get_url = ""

    # Define the header(s)
    # Use the following API Key: live_NMNC1lcbODoViW3HxtYkiIstzdDd8wN2e8tlHLM6QyDGSKTA1NUGGdqEGP7UOoBm
    get_headers = {}

    # Create the request using the correct method from the requests library
    #response = 

    # Print the URL to the image
    print("Challenge 1: Below is the URL to a random cat image")
    print(response.json()[0]["url"])

# -- Edit this function -- #
def favorite_image():
    """
    Favorites a cat image

    Link to Documentation: https://documenter.getpostman.com/view/5578104/RWgqUxxh#ae1b5e8f-ca63-4de8-a715-f4944f4cec07
    """

    # Define the full URL
    post_url = ""

    # Define the header(s)
    # Use the following API Key: live_NMNC1lcbODoViW3HxtYkiIstzdDd8wN2e8tlHLM6QyDGSKTA1NUGGdqEGP7UOoBm
    post_headers = {}

    # Define the data to send. You need to only use the `image_id` key and use the ID: h-bMdWYmd
    post_data = {}

    # Create the request using the correct method from the requests library
    #response = 

    print("Challenge 2: You should get a 'SUCCESS' message below")
    print(response.text)

# -- DO NOT EDIT BELOW THIS LINE -- #
if __name__ == "__main__":
    # try to execute the get request
    try:
        get_image()
    except Exception as e:
        print(e)

    # try to execute the post request
    try:
        favorite_image()
    except Exception as e:
        print(e)