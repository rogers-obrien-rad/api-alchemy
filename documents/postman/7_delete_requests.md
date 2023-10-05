# HTTP DELETE REQUESTS

You will likely be using Postman to try out third-party APIs by making HTTP requests according to their documentation. These section will walk you through the steps to make your first HTTP DELETE request with Postman!

> It is important to follow this article from top-to-bottom. Some of the latter requests might require setup that is done in a previous step.


## EXAMPLE API: RESTFUL BOOKER

We will be using the [Restful Booker API](https://restful-booker.herokuapp.com/) again to delete our fake hotel bookings to showcase DELETE requests in Postman.

## ﻿SETUP

Before we start making DELETE requests, you need to be able to create data so that we can delete it i.e. create POST requests. Check out the [Postman: POST Requests](https://github.com/rogers-obrien-rad/api-alchemy/blob/main/documents/postman/5_post_requests.md) article which covers the necessary setup.


## CREATE AUTH TOKEN

> This step is also covered in [Postman: PATCH Requests](https://github.com/rogers-obrien-rad/api-alchemy/blob/main/documents/postman/6_patch_requests.md)

Before we can update our booking, we have to get authorization from the server in the form of a Token. To do this, we have to make a POST request with some fake credentials.


### INITIALIZE REQUEST

The Restful Booking endpoint to create an Auth Token is:

```
https://restful-booker.herokuapp.com/auth
```

and the documentation can be found [here](https://restful-booker.herokuapp.com/apidoc/index.html#api-Auth-CreateToken)

 1. Use the "+" button﻿﻿ to create a new request.
 2. This time, we are going to be creating a POST so select the dropdown that currently says "GET" and choose the option for "POST".
 3. Copy the URL above and paste it into Postman. Save the request as "Create Token" to the "Hotel Booking" collection you should have created in the Setup step of the [Postman: POST Requests](https://github.com/rogers-obrien-rad/api-alchemy/blob/main/documents/postman/5_post_requests.md) article.


### ADD HEADER

 1. We now have to include the `Content-Type` in the request Headers. When you save the request as a POST request, you will have a few Headers that are automatically created. You can view them by selecting the Headers tab:

﻿﻿﻿![image1](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/d90dc9b8-ab8c-4676-9fbb-c283f8239baa)

 2. We need to add a `Content-Type` Header. Click the "Key" text in the bottom row and type in "Content-Type" and in the "Value" column add "application/json" because we are going to be sending JSON data in our request. You will notice that as you type, Postman will suggest options for you that you can select. Your table should now look like this:

![image2](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/ebbc3286-b1ff-4b1d-8dc2-580812f758c9)

### ADD BODY

Next we will need to add the body data which will contain the information regarding the booking.

 1. Select the "Body" tab on the "Create Booking" request.
 2. We specified `application/json` in the Header previously, so select the radio button for "raw" and you should see a text entry box appear and a blue-text dropdown with "JSON" currently active:

![image3](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/e84c2aad-b55a-4248-bddf-93210fd92c97)

 3. Now we just have to paste in JSON data that includes the username and password of the user. We don't have to register for anything, but can use some fake credentials that anyone can use:

```json
{
    "username" : "admin",
    "password" : "password123"
}
```

### SEND REQUEST

With the Headers and Body setup, it is time to create an Auth token to use.

 1. ﻿Save the request
 2. Hit the blue "Send" button﻿﻿﻿
 3. Assuming everything went smoothly, you should get a 200: OK status code and JOSN data with one key-value pair:

![image4](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/a78648fa-5cf6-4108-ab32-dcf179dbe4ed)

## CREATE DELETE BOOKING REQUEST

Now that we have a method of creating an Auth Token, we can Authenticate our request to delete a booking.


### INITIALIZE REQUEST

The Restful Booking endpoint to update a booking is:

```
https://restful-booker.herokuapp.com/booking/:id
```

and the documentation can be found [here](https://restful-booker.herokuapp.com/apidoc/index.html#api-Booking-DeleteBooking)

 1. Use the "+" button﻿﻿﻿ to create a new request.
 2. Copy the URL above, paste it into Postman, and select the dropdown that currently says "GET" and choose the option for "DELETE".
 3. Save the request as "Delete Booking" to the "Hotel Booking" collection you should have created in the Setup step.

### SPECIFY PATH PARAMETER

You might have noticed that when you copied the URL above, the "Params" section of the "Update Booking" request updated to include a Path Variables section with a Key of `id`. This happened because Postman recognizes anything preceded by a colon as a Path Variable.

We need to specify the `id` Path Parameter with the ID of the booking we just created, but we will do that at a later time because we will need to stack our requests and run them in a timely fashion. For now, you can just leave the "Value" column blank.


### ADD HEADER

We need to add a header to contain the Auth Token. The documentation says we have two options, but we are going to use the `Cookie` header.

 1. Navigate to the Headers tab in the "Update Booking" request.
 2. In the bottom row, add a Key of "Cookie" and for the value, enter "token=". We will add the actual token value in a later step.

When you are done adding the headers, your table should look like the following:

![image5](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/79e3ab7e-6988-42c9-a018-f847019a58d7)

## SEND THE DELETE BOOKING REQUEST

Executing the "Update Booking" request requires we send three requests back-to-back-to-back, modifying parameters in the last request based on the two previous requests. This process can be automated, but is beyond the scope of these entry articles. In short, we will:

 1. Create a booking with the "Create Booking" POST request
 2. Get an Auth Token using the "Create Token" POST request
 3. Delete the Booking from Step 1 by using the Booking ID and the Auth Token


### CREATE A BOOKING

Create a booking using the "Create Booking" POST request described in the [Postman: POST Requests](https://github.com/rogers-obrien-rad/api-alchemy/blob/main/documents/postman/5_post_requests.md) article. After you have done so, make sure to note the `bookingid` in the response body:

![image6](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/ea9bc67d-c003-4f9a-b1be-13a3c1b0b62e)

### CREATE AN AUTH TOKEN

Now use the "Create Token" POST request we made in this article to generate a new Auth Token for you. Make sure to copy this token for the last step:

![image7](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/e10b5757-4a57-46bc-875b-ee6a70b86023)

### DELETE BOOKING

Finally, we can delete our booking:

 1. Under the Params tab in the "Delete Booking" DELETE request, update the Value column in the Path Variables table to match the `bookingid` you just got from Step 1.
 2. Under the Headers tab in the "Update Booking" DELETE request, update the `Cookie`
    value to include the Auth Token from Step 2 . Do not include the quotation marks, but be sure to include the "token=" part. Your Value column should look something like what is shown below but with your own unique token:

```
token=fc0c93bc6122ab9
```

 3. Save the request and hit the blue "Send" button﻿﻿
 4. If everything went smoothly, you should get a 201: Create status code and a message that simply states "Created":

![image8](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/5a157db9-1e8c-4ac9-89b5-f6bbd205c0d4)
