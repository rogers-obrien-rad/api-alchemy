# HTTP GET REQUESTS

You will likely be using Postman to try out third-party APIs by making HTTP requests according to their documentation. These section will walk you through the steps to make your first HTTP requests with Postman!

> It is important to follow this article from top-to-bottom. Some of the latter requests might require setup that is done in a previous step.


## EXAMPLE API: REST COUNTRIES

We will be using the [REST Countries API](https://restcountries.com/#rest-countries) to send GET requests.



## SETUP

Before we start making GET requests, let's create a new collection so that we can store these requests in one location and have a place where we can specify the variables we will need. You can learn how to create a new collection by referencing our [Postman: Collections](https://github.com/rogers-obrien-rad/api-alchemy/blob/main/documents/postman/collections.md) article.

 1. Create a collection called "Countries". We will save requests to this collection and create variables within it to reference in some requests.




## THE SIMPLEST GET REQUEST

For most public APIs, there are some endpoints that require no configuration; you simply have to send a request to a given HTTP endpoint and you get data back! This request will be the first one we do.

 1. Start by clicking the "+" icon to create a new tab. You should now see a window like this in the center:

![image1](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/7d7115ad-6087-4a29-8c37-ede13079bd13)


 2. We are going to list all countries that are in the REST Countries API. We can do that by using the [all](https://restcountries.com/#endpoints-all) endpoint:

```
https://restcountries.com/v3.1/all
```

 3. Copy the text above and paste it in the textbox next to the green GET dropdown:

![image2](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/e9905ab6-274a-4aff-ba67-a6478c3f253b)


 4. That is all we need for this endpoint, so click the blue "Send" button!
 5. If everything goes smoothly, you should see the body payload returned in the response. It will look something like this:

![image3](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/9951256d-1b69-4461-8140-44880170b6c6)


 6. Find the "Save" button or hit "ctrl"+"s" on your keyboard to save the request as "List All" to the "Countries" collection you should have created in the Setup step.


## REVIEWING THE RESPONSE

There are a few components of the response that we should review before looking at more complicated GET requests. We will use the previous request as an example. There are a few options you can toggle through at the top right of the response window:

![image4](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/c27b4cc1-416e-42d8-916f-ec46e2ad5aa4)

We will look into the "Body" and "Headers" sections more.

### RESPONSE BODY

The default window that will be shown at the bottom in the response will be the body. Typically the body will be JSON data, but sometimes will be the status code in a message, especially if there was a 400 error.

Within the "Body" window, you have the option to see the body in different formats. "Pretty" is likely the only one you need to worry about. The dropdown allows you to specify the data type, but most of the time the program is smart enough to select the right one for you:

![image5](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/b61139e8-b7c9-4f7a-bba0-b3401ce41d60)


In the example, the program selected JSON format. Often times, the data type is specified in the response headers so that is why Postman is usually able to correctly select the correct data type to display in "Pretty".


### RESPONSE HEADERS

The response headers often provide some valuable information that you might want to view. Select "Headers (#)" to show the key-value pairs:

![image6](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/77f2bde4-d47b-4850-859b-ce50d46879cd)

In this example, the response had 8 headers. Most of them are not important for our purposes, but headers like `Content-Type` are common across all APIs while others such as `content-length` might be unique to the API you are using.


#### HTTP REQUEST DETAILS

At the top-right of the response window, you should see some more details like this:

![image7](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/f21bf482-2875-48e5-9376-d27f9f5d0cf5)


This banner provides valuable insight regarding the request you sent. "Time" and "Size" are self-explanatory, but "Status" can vary and is arguably the most important. You can see a full list of [status codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) by searching them on the internet, but generally:

 * 200s: The request was successfully executed
 * 400s: Something was wrong with the request you (the client) sent
 * 500s: Something went wrong with the program (the server) when it tried to process your request


## USING PATH PARAMETERS

Path parameters are variables that are placed directly in the HTTP request endpoint. In Postman, you can hardcode the value you would like into the path or use variables. This section will show you both.

The REST Countries API allows you to [specify which country you want to view](https://restcountries.com/#endpoints-name) by including the country's name in the path. The end point looks like:

```
https://restcountries.com/v3.1/name/{name}
```

Where `{name}` is a path parameters where you specify the country's name.

 1. Click the "+" icon to create a new GET request
 2. Copy and paste the endpoint above into the endpoint, but replace `{name}` with "deutschland":

![image8](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/afb1b0dc-4576-41f4-9d38-fe68e87dd4ae)

 3. Click the "Send" button and you should see a lot of data about Germany in the response body assuming you get a 200: OK status
 4. Save the request as "Single Country" to the "Countries" collection

This process worked just fine, but what if you had multiple requests that referenced the same country name? You would have to go to each request and type in the new country name every time you changed it. Rather than do that, you could specify a collection variable and have each request reference that variable. Then you just have to change the value of the variable and all your requests will update! We will highlight this in the next section. For now, let's just create the variable.

The steps to create a variable from a request specification are given in [Postman: Collections](https://github.com/rogers-obrien-rad/api-alchemy/blob/main/documents/postman/collections.md), so we will be brief when describing how to create a variable here. For more in-depth description, reference that article.

 1. Ensure you have saved the request as "Single Country" to the "Countries" collection
 2. Highlight "deutschland" with your cursor and you should see a pop-up that says "Set as variable" - click this.
 3. Name the variable `country`, ensure the value is "deutschland", and set the scope to the "Countries" collection.

Now the "Countries" collection has a `country` variable we can reference. Your endpoint should now look slightly different:

![image9](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/76a5b279-93e9-45b8-ba01-7eefda0254ba)


## USING QUERY PARAMETERS

Query parameters are used often in GET requests and Postman makes using them fairly straight-forward.

Right now when we get data for a country, there is a lot of information that we don't need. Luckily, the REST Countries API has a filtering option that makes use of query parameters:

```
https://restcountries.com/v3.1/{service}?fields={field},{field},{field}
```

Where:

 * `{service}` is the specific endpoint like the `name` that we used earlier and;
 * `{field}` is one of the various fields returned in the body of the response

 1. Start by creating a new request by clicking "+" icon
 2. Name this request "Name, Region, and Capitol"﻿ and save it to the "Countries" collection
 3. Copy and paste the endpoint above into the request endpoint and make sure you are doing a GET request (the default)
 4. You might've noticed that after you pasted in the endpoint, the query parameters table updated with a `fields` parameter (see below). Postman is able to do this because query parameters come after the endpoint and any path parameters and are denoted by a question mark (?). Multiple query parameters are separated by an ampersand (&).

![image10](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/755ad244-4deb-43a1-be9b-aeb23552d867)

> Regretably, this example is a bit confusing but we are only using one query parameter, but the value of that parameter is a list. We are not using multiple parameters hence no "&".

 5. Replace `{service}` with "/name/{{country}}" and make sure the "?" is directly after the closing double curly braces.
 6. Replace `{field},{field},{field}` with "name,continent,capital" - make sure there are now space. You can replace the `{field},{field},{field}` value either in the endpoint URL or in the table. You should notice that as you edit one of the two options, the other one updates too!
 7. Once you have replaced both the path parameter and query parameter values, click the "Send" button
 8. You should have gotten some data in the response body and a 200 OK status code. However, if you look closely, you will see there is no information about the continent. If you go through the fields in the JSON response data from the "Single Country" request, you will notice there isn't a field called "continent", but there is a "region" which appears to show the continent. Specifying the wrong query parameters and values tends to be okay and won't cause a 400 error. However, it could lead to problems down the road since you got a 200 status code, but the data you got back wasn't entirely correct.

 9. Replace "continent" with "region" in your query parameters and send the request again. You should get the following response body:

```json
[
    {
        "name": {
            "common": "Germany",
            "official": "Federal Republic of Germany",
            "nativeName": {
                "deu": {
                    "official": "Bundesrepublik Deutschland",
                    "common": "Deutschland"
                }
            }
        },
        "capital": [
            "Berlin"
        ],
        "region": "Europe"
    }
]
```

## LEVERAGING POSTMAN VARIABLES

Let's say we wanted to run these two requests but for the United States. We can update both requests by changing the collection variable `country` and then running them again.

 1. On the sidebar, make sure Collections is highlighted.
 2. Select the "Countries" collection and click on the "Variables" tab.
 3. Change the current value of country to "usa". We don't have to change the initial value since it isn't actually used in the request. Make sure to click the "Save" button!
 4. Run the "Single Country" and "Name, Region, and Capital" requests again and notice how the response data has changed to USA data:

```json
[
    {
        "name": {
            "common": "United States",
            "official": "United States of America",
            "nativeName": {
                "eng": {
                    "official": "United States of America",
                    "common": "United States"
                }
            }
        },
        "capital": [
            "Washington, D.C."
        ],
        "region": "Americas"
    }
]
```

---
