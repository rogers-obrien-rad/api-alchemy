import requests

# -- Edit this function -- #
def get_image():

    # Define the full URL
    url = ""

    # Define the header(s)
    headers = {}

    # Create the request using the correct method from the requests library
    #response = 

    # Print the URL to the image
    print(response.json()[0]["url"])

# -- Edit this function -- #
def favorite_image():

    # Define the full URL
    url = ""

    # Define the header(s)
    headers = {}

    # Define the data to send. You need to only use the `image_id` key and use the ID: h-bMdWYmd
    data = {}

    # Create the request using the correct method from the requests library
    #response = 

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