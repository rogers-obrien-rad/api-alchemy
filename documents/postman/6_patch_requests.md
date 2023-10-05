# HTTP PATCH REQUESTS

You will likely be using Postman to try out third-party APIs by making HTTP requests according to their documentation. These section will walk you through the steps to make your first HTTP PATCH request with Postman!

> It is important to follow this article from top-to-bottom. Some of the latter requests might require setup that is done in a previous step.

## EXAMPLE API: RESTFUL BOOKER

We will be using the [Restful Booker API](https://restful-booker.herokuapp.com/) again to update our fake hotel bookings to showcase PATCH requests in Postman.

## SETUP

Before we start making PATCH requests, you need to understand how to create data to modify i.e. create POST requests. Check out the [Postman: POST Requests](https://github.com/rogers-obrien-rad/api-alchemy/blob/main/documents/postman/5_post_requests.md) article which covers the necessary setup.

## CREATE AUTH TOKEN

> This section is covered in [Postman: DELETE Requests]()

Before we can update our booking, we have to get authorization from the server in the form of a Token. To do this, we have to make a POST request with some fake credentials.

### INITIALIZE REQUEST

The Restful Booking endpoint to create an Auth Token is:

```
https://restful-booker.herokuapp.com/auth
```

and the documentation can be found [here](https://restful-booker.herokuapp.com/apidoc/index.html#api-Auth-CreateToken).

 1. Use the "+" button﻿ to create a new request.
 2. This time, we are going to be creating a POST so select the dropdown that currently says "GET" and choose the option for "POST".
 3. Copy the URL above and paste it into Postman. Save the request as "Create Token" to the "Hotel Booking" collection you should have created in the Setup step of the [Postman: POST Requests](https://github.com/rogers-obrien-rad/api-alchemy/blob/main/documents/postman/5_post_requests.md) article.


### ADD HEADER

 1. We now have to include the `Content-Type` in the request Headers. When you save the request as a POST request, you will have a few Headers that are automatically created. You can view them by selecting the Headers tab:

﻿﻿![image1](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/5dfa939e-3835-4983-a1c7-0fea98886f4c)

 2. We need to add a `Content-Type` Header. Click the "Key" text in the bottom row and type in "Content-Type" and in the "Value" column add "application/json" because we are going to be sending JSON data in our request. You will notice that as you type, Postman will suggest options for you that you can select. Your table should now look like this:

![image2](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/296d83fb-5d89-4d41-9319-d9da9ad56b5e)

### ADD BODY

Next we will need to add the body data which will contain the information regarding the booking.

 1. Select the "Body" tab on the "Create Booking" request.
 2. We specified `application/json` in the Header previously, so select the radio button for "raw" and you should see a text entry box appear and a blue-text dropdown with "JSON" currently active:

![image3](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/9daac8e9-bd07-4202-b1b3-330a907726bd)

 3. Now we just have to paste in JSON data that includes the username and password of the user. We don't have to register for anything, but can use some fake credentials that anyone can use:

```json
{
    "username" : "admin",
    "password" : "password123"
}
```


### SEND REQUEST

With the Headers and Body setup, it is time to create an Auth token to use.

 1. ﻿Use the "Save" button to save the request
 2. Hit the blue "Send" button﻿﻿
 3. Assuming everything went smoothly, you should get a 200: OK status code and JOSN data with one key-value pair:

﻿﻿![image4](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/0f01781d-fcd9-41eb-81d2-101a11cba9c5)

## ﻿SETUP UPDATE BOOKING REQUEST

Now that we have a method of creating an Auth Token, we can Authenticate our request to update a booking.

### INITIALIZE REQUEST

The Restful Booking endpoint to update a booking is:

```
https://restful-booker.herokuapp.com/booking/:id
```

and the documentation can be found [here](https://restful-booker.herokuapp.com/apidoc/index.html#api-Booking-PartialUpdateBooking)

 1. Use the "+" button﻿﻿ to create a new request.
 2. Copy the URL above, paste it into Postman, and select the dropdown that currently says "GET" and choose the option for "PATCH".
 3. Save the request as "Update Booking" to the "Hotel Booking" collection you should have created in the Setup step.


### SPECIFY PATH PARAMETER

You might have noticed that when you copied the URL above, the "Params" section of the "Update Booking" request updated to include a Path Variables section with a Key of `id`. This happened because Postman recognizes anything preceded by a colon as a Path Variable.

We need to specify the `id` Path Parameter with the ID of the booking we just created, but we will do that at a later time because we will need to stack our requests in and run them in a timely fashion. For now, you can just leave the "Value" column blank.


### ADD HEADERS

We need to add two Header parameters.

The first Header parameter is the `Content-Type` since we will be sending new data to update the booking with. Again, we are going to be using JSON data.

 1. Navigate to the Headers tab in the "Update Booking" request.
 2. In the bottom row, add a Key of "Content-Type" and for the value, enter "application/json".

The second header will contain the Auth Token. The documentation says we have two options, but we are going to use the `Cookie` header.

 1. Navigate to the Headers tab in the "Update Booking" request.
 2. In the bottom row, add a Key of "Cookie" and for the value, enter "token=". We will add the actual token value in a later step.

When you are done adding the headers, your table should have these two rows at the bottom:

![image5](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/5c5ef6b8-8d15-4dd0-9e54-6a365accc466)

### ADD BODY

The last thing we need to do is create a the request body using JSON format. We are going to keep it simple and just change the name on the reservation. Feel free to modify the JSON below, but make sure both the first and last names are different that what you have been using for the "Create Booking" request in [Postman: POST Requests](https://github.com/rogers-obrien-rad/api-alchemy/blob/main/documents/postman/5_post_requests.md):

```json
{
    "firstname" : "James",
    "lastname" : "Holmes"
}
```

Your Body tab should look like the following:

![image6](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/a41e4c9b-3e15-4d54-b846-3881f2a3f37a)

## SEND THE UPDATE BOOKING REQUEST

Executing the "Update Booking" request requires we send three requests back-to-back-to-back, modifying parameters in the last request based on the two previous requests. This process can be automated, but is beyond the scope of these entry articles. In short, we will:

 1. Create a booking with the "Create Booking" POST request
 2. Get an Auth Token using the "Create Token" POST request
 3. Update the Booking from Step 1 by using the Booking ID and the Auth Token


### CREATE A BOOKING

Create a booking using the "Create Booking" POST request described in the [Postman: POST Requests](https://github.com/rogers-obrien-rad/api-alchemy/blob/main/documents/postman/5_post_requests.md) article. After you have done so, make sure to note the `bookingid` in the response body:

![image7](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/a2d1adff-30bb-4350-8c39-6ff9acaed4ae)

### CREATE AN AUTH TOKEN

Now use the "Create Token" POST request we made in this article to generate a new Auth Token for you. Make sure to copy this token for the last step:

![image8](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/afaf3285-8d7d-4bc3-8120-48e698dfbfa5)

### UPDATE BOOKING

Finally, we can update our booking:

 1. Under the Params tab in the "Update Booking" PATCH request, update the Value column in the Path Variables table to match the `bookingid` you just got from Step 1.
 2. Under the Headers tab in the "Update Booking" PATCH request, update the `Cookie` value to include the Auth Token from Step 2 . Do not include the quotation marks, but be sure to include the "token=" part. Your Value column should look something like what is shown below but with your own unique token:

```
token=fc0c93bc6122ab9
```

 3. Save the request and hit the blue "Send" button
 4. If everything went smoothly, the response body should include the same information from the "Create Booking" POST request but with a new `firstname` and `lastname`:

﻿![image9](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/4b719b0c-5e76-4faf-aab2-b5d1bd89816b)

 ---
