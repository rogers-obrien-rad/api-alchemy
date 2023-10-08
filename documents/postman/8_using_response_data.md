# Using Response Data
Often times you will send a GET request and need to use the data in the response for other requests, such as when you fetch an access token and need to use that token for authorization. Postman has a way of parsing the response data and then setting a variable's value based on something in that response.


## EXAMPLE API: POKEAPI

We will be using the [PokeAPI](https://pokeapi.co/) to get info about Pokemon and use that info to help send other requests.

## SETUP

Before we start , let's create a new collection so that we can store these requests in one location and have a place where we can specify the variables we will need. You can learn how to create a new collection by referencing our [Postman: Collections](https://github.com/rogers-obrien-rad/api-alchemy/blob/main/documents/postman/3_collections.md) article.

 1. Create a collection called "Pokemon". We will save requests to this collection and create variables within it to reference in some requests.

## GET A POKEMON
We are going to start with a simple GET request to get information about a Pokemon using the following endpoint:

```
https://pokeapi.co/api/v2/pokemon/:name
```

 1. Start by clicking the "+"﻿ icon to create a new tab.
 2. Copy the URL above into the GET text entry.
 3. A new Path Variables table should have been created for you with a Key of "name". For the Value, let's choose the classic "pikachu":

![image1](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/7feac051-5ed5-47d8-bebe-204a8cbd8d3c)

 4. Save the request as "Pokemon" to the "Pokemon" collection you made in the Setup step and then click the blue "Send" button.
 5. You should get a lengthy JSON response with everything you ever wanted to know about Pikachu.

## CREATE COLLECTION VARIABLES

We are going to create some collection variables that we will use in later requests and that we will have dynamically update by parsing response data.

 1. Click on the "Pokemon" collection and select the "Variables" tab.

![image2](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/4b3d3e09-d51b-4b6b-8ef1-c1c13e7530df)


 2. Create a variable "first_move" and use "tackle" as the Initial and Current Values.
 3. Create a variable "primary_type" and use "normal" as the Initial and Current Values.
 4. Save your changes with "ctrl"+"s" and you variable table should look like this:

![image3](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/ba5dd207-1cb7-4ebe-8303-0fc4525548f7)

## PARSE RESPONSE DATA

Postman gives us a way of executing JavaScript code which can access data about the request and response.

 1. Navigate to the "Tests" tab of the "Pokemon" GET request we just made. You should see a blank text entry field with a small side panel with some "Snippets":

![image4](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/25951e2c-f3ca-48ba-960c-9f58e18ebaa4)


 2. This entry will be where you can write JavaScript code and the "Snippets" provide ready-to-use code to help you get started. We will use a snippet in a later step, but for now we need to get the response data saved in a variable so that we can access different aspects of it. The `pm.response` object contains the JSON data that was returned to us in the response. Start by typing:

```javascript
var jsonData = pm.response.json();

```

Now we will have access to the response data in the `jsonData` variable.

 3. We want to set the `first_move` collection variable to the first move given in the "moves" key. Luckily, Postman provides a nice snippet to help us get started. On the right, scroll until you see the option for "Set a collection variable" and click it. You should see the following code appear in the text entry box wherever your cursor was:

```JavaScript
pm.collectionVariables.set("variable_key", "variable_value");
```

 4. Replace `variable_key` with `first_move` (and keep the double quotes).
 5. For the `variable_value` we are going to have to use the `jsonData` variable and traverse the "moves" key which looks like:

```json
moves:
  0:
    move:
      name: "mega-punch"
      url: "https://pokeapi.co/api/v2/move/5/"
      version_group_details: [5]
  1: {…}
```

To access the value in `name`, we need to access the "moves" key, then "0", then "move", and finally "name". To do this, we place these keys in square brackets behind the variable `jsonData`:

```JavaScript
jsonData["moves"]["0"]["move"]["name"]
```

 6. Your script should look like the following:

```JavaScript
var jsonData = pm.response.json();

pm.collectionVariables.set("first_move", jsonData["moves"]["0"]["move"]["name"]);
```

 7. We need to do the same thing but for `primary_type`. The structure for the "types" key is similar to "moves":

```json
types:
  0:
    slot: 
    type:
      name: "electric"
      url: "https://pokeapi.co/api/v2/type/13/"
```

So to access the name of the primary type, we would do:

```JavaScript
jsonData["types"]["0"]["type"]["name"]
```

 8. Insert a new line into your script by either copying/pasting the line you used to set the `first_move` variable or clicking the snippet option for "Set a collection variable". For the variable name, use `primary_type` and use the code above for the value. Your final script should look like the following:

```JavaScript
var jsonData = pm.response.json();

pm.collectionVariables.set("first_move", jsonData["moves"]["0"]["move"]["name"]);
pm.collectionVariables.set("primary_type", jsonData["types"]["0"]["type"]["name"]);
```

 9.  Click the blue "Send" button.
 10. Check the "Current Value" of the `first_move` and `primary_type` variables in the "Pokemon" collection "Variables" tab. Your table should now have the updated values of "mega-punch" and "electric":

![image5](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/89881255-9cd3-4916-825e-67bbb60e1222)

## CONNECT DYNAMIC VARIABLES TO NEW REQUEST

Now that the `first_move` and `primary_type` variables update anytime we run the "Pokemon" GET request with a new Pokemon, we can tie in some other requests.

### CREATE NEW REQUEST

Let's use a GET request to learn more about a move which can be done with the following endpoint:

```
https://pokeapi.co/api/v2/move/:name
```

 1. Start by clicking the "+"﻿﻿ icon to create a new tab.
 2. Copy the URL above into the GET text entry.
 3. Save the request as "First Move" in the "Pokemon" collection.

 4. A Path Variables table should have been created for you with a Key of "name". For the Value, let's choose the variable `first_move`, which you can specify by starting with two curly brackets `{{`:

![image6](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/98a9e88c-b30d-4f6d-8a9d-cdc44ae54764)

### GET MOVE RESPONSE

 1. Click the blue "Send" button and review the response.
 2. You should get a lengthy response with the "accuracy" key at the very top with a value of 85.


### UPDATE POKEMON AND GET NEW MOVE RESPONSE

Now we are going to see what happens when we choose a new Pokemon.

 1. Go back to the "Pokemon" get request and let's specify "bulbasaur" as the "name" Path Variable:

![image7](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/138b0b66-0920-4146-ba16-23e7d3823641)


 2. Hit the blue "Send" button to run this request again.
 3. The `first_move` and `primary_type` variables should have updated.
 4. Open the "First Move" request and hit the blue "Send" button.
 5. Your response should have changed and now you see the "accuracy" value is 100.
 6. Navigate to the "Pokemon" collection and click the Variables tab. You should see that `first_move` and `primary_type` have changed:

![image8](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/7987af60-fcc8-4b21-a33b-dc042c7aad5b)

You can use JavaScript scripting to help automatically update variables and other Postman components. Rather than having to manually update these values any time you changed a request that subsequent requests depended on.
