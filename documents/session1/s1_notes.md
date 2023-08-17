# Session 1: Introduction to APIs and API Basics (2 hours) 👨‍🏫
_Gain an understanding of APIs and their role in modern software development, along with exploring the fundamental concepts of REST and SOAP methods._

## Subsection 1: [Introduction and What are APIs?](https://github.com/rogers-obrien-rad/api-alchemy/blob/main/documents/session1/s1_agenda.md#introduction-and-what-are-apis-10-minutes)

### Slide 1: Title

### Slide 2: Agenda
* Provide an overview of the topics that will be discussed during this session
* Be sure to point out that numbers refer to the approximate time in minutes

### Slide 3: Course Introduction
_General overview of what to expect from the class_
* **Objective**: Learn about what APIs are, what they can do for you, and how to leverage them
* **Hands-On Learning**: Stress that these sessions will always have a significant portion dedicated to hands-on, guided learning so that the topics can stick a bit more.
* **Open Discourse**: Questions are highly encouraged at any point, but be respectful to others if we are going over. Hagen is always available to discuss more on a topic outside of the session. If an answer is not known, Hagen will find it and share with the class at a later time.
* **Structure**: Training is broken into four 2-hour sessions with a 10-minute break provided around the midpoint of the session.

### Slide 4: Definition of APIs
_Overview of what an API is with examples_

> An Application Programming Interface is a set of protocols that allows different software applications to communicate, interact, and share data with each other.
* Watch [video](https://www.youtube.com/watch?v=s7wmiS2mSXY)
* Additional examples of APIs
  * **Weather Apps**: Weather apps use APIs to access real-time weather data from external sources. These APIs provide accurate and up-to-date information. By leveraging APIs, weather apps avoid the need to collect and maintain their own weather data.
  * **Social Media**: When you click "Share", an API is invoked, sending the data to the respective social media platform. The platform's API processes the request, posts the content, and provides feedback to the user.
  * **Payment Apps**: When you initiate a payment, the app sends transaction details to the payment gateway's API. The API handles payment authorization, processes the transaction, and returns a response to the app

## Subsection 2: [Advantages of Using APIs](https://github.com/rogers-obrien-rad/api-alchemy/blob/main/documents/session1/s1_agenda.md#advantages-of-using-apis-10-minutes)

### Slide 5: Advantages of APIs

#### Efficiency
* **Time savings**: No manual data entry and no manual code development. Simply use the API to pull the data you need.
* **Interoperability**: APIs allow you to interface with the main platform using a variety of applications. You can use almost any popular programming language and there are services that we will use later that make the job even easier. 
* **Scalability**: You aren't storing the data on your device or in your application which allows your application to run faster and you don't have to deal with paying for storage. 

#### Innovation
* **Integrate faster**: You are relying on other people who are likely more experienced software developers to create pathways to the data you want. Once those pathways are created, you can quickly push and/or pull the data you need. You can also leverage their platform to get things like continuous and real-time updates.
* **Integrate more**: You can scale up the amount of information you pull into your application by using APIs from a wide variety of platforms to provide a richer experience.

#### Cost and Flexibility
* **Save costs and resources**: You can focus on the analysis side of things rather than the data gathering. Or you can discover ways to use the API to speed up your process that aren't available on the UI. 
* **Reduced maintenance**: If you created your process to push or pull data, you would personally need to maintain that. If you use APIs, the platform will ensure that these pathways remain stable even if they change how their front- or back-end works. 
* **Choose what you need**: API pathways are generally specific to what functions they can accomplish. Rather than doing bulk actions that could be time-consuming or provide excessive information, you can do exactly what you like. 

### Slide 6: Case Studies

#### [McBroken](https://mcbroken.com/)
_The McBroken app uses the McDonald's API to track the availability of working ice cream machines at various locations in real-time, providing users with up-to-date information on whether they can get frozen treats._
* Software Developer reverse-engineered the McDonald's ordering API to send an order worth $18,752 of McFlurries to every McDonald's in the US
* Based on whether the item can be added to your cart determines if the machine is working or not

#### Pokemon Go
_Pokémon Go is an augmented reality mobile game that uses real-world locations and the camera on players' smartphones to allow them to catch virtual Pokémon in their surroundings._
* Utilizes the Google Maps API to display Pokemon in your environment

#### Procore Permissioning
_Procore is a cloud-based construction management platform that provides tools for project management, collaboration, scheduling, and financial management._
* Procore provides permissions templates that sometimes can only be applied on a per-person basis meaning that.
* If we wanted to specify _everyone's_ permissions for a given project, someone would have to go through each individual and update their permissions.
* We can use the Procore API to do this for us by automating the process. We still have to go one-by-one, but the computer can change someone's permissions in a matter of milliseconds while it might take a user 10 seconds to do the same process (not to mention it would be incredibly boring). 

## Subsection 3: [API Basics](https://github.com/rogers-obrien-rad/api-alchemy/blob/main/documents/session1/s1_agenda.md#api-basics-rest-and-soap-10-minutes)

### Slide 7: API Architecture
_How the rules of an API are setup to ensure smooth communication_

#### REST (Representational State Transfer):
* Modern and simple way for software to communicate over the internet
* Communication is like talking to a waiter: you ask for things (GET), give new things (POST), update (PUT), or remove (DELETE)
* Simple and straightforward
* Uses URLs to represent different resources (like menu items), and you use different actions (HTTP methods) to interact with those resources

#### SOAP (Simple Object Access Protocol):
* Like sending a package with instructions and details
* More structured and formal than REST
* Often used in big businesses
* Communication is more like writing a letter: you need to follow specific rules
* Can use different delivery methods (transport protocols) like HTTP, SMTP (email), etc.
* Has a fixed structure (XML) for messages, making sure everyone understands the message format

### Slide 8: SOAP Overview
* **Principle**: Uses more formal rules, like sending a detailed package with instructions.
* **Use Cases**: Suited for complex applications, often used in big businesses and industries where strict communication is needed.
* **Advantages**: Structured and secure. Provides strict standards for messaging and security, suitable for enterprise scenarios.
* **Disadvantages**: Heavier and more complex compared to REST. May not be suitable for lightweight applications.

### Slide 9: REST Overview
* **Principle**: Uses simple rules to communicate over the internet, like talking to a waiter to order food.
* **Use Cases**: Best for simpler applications like mobile apps and websites, where quick communication is important.
* **Advantages**: Easy to understand, lightweight, and flexible. Works well for microservices and modern web applications.
* **Disadvantages**: Less structured than SOAP, not ideal for complex enterprise-level applications.

### Slide 10: Process Overview


## Subsection 4: [HTTP](https://github.com/rogers-obrien-rad/api-alchemy/blob/main/documents/session1/s1_agenda.md#restful-api-concepts-and-http-methods-15-minutes)

### Slide 11: HTTP Structure

#### Start Line
_First line of the request/response_

For requests, the start line is called the "Request Line" and includes:
* HTTP method
* URL of the resource being requested
* Parameters
* version of the HTTP protocol being used

For responses, the start line is called the "Status Line" and includes:
* three-digit status code
* text description of status
* version of the HTTP protocol being used

#### Headers
_Additional lines that include important, standardized information for the HTTP request/response_

You can find available Header options [here](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields), but some of the more common ones include:
* **Authorization**: credentials
* **Content-Type**: media type for the body of the request/response
* **Host**: domain name of the server i.e. google.com

#### Blank Line
_Tells the program that the previous values were for the header while the following are for the body_

#### Body
_Optional component that carries additional data sent with the request/response, such as form data or request payload._

For requests, the body is often formatted in:
* JSON
* XML

For responses, the body is often formatted in:
* JSON
* XML
* HTML

### Slide 12: HTTP Methods
_The data manipulation methods used by APIs_

There are [9 HTTP methods in HTTP v1.1](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods), but there are four/five ones that are commonly used:
* **POST**: Used to send data to the server, for example, customer information, file upload, etc.
* **GET**: Used to retrieve information from the given server using a given URI. Requests using GET should only retrieve data and should have no other effect on the data.
* **PUT**: Replaces all current representations of the target resource with the uploaded content.
* **PATCH**: Applies partial modifications to a resource.
* **DELETE**: Removes the specified resource.

### Slide 13: Response Status Codes
_Status of the HTTP request_

#### 100s - Informational
An informational response indicates that the request was received and understood. It is issued on a provisional basis while request processing continues. It alerts the client to wait for a final response.

#### 200s - Success
These status codes indicates the action requested by the client was received, understood, and accepted. Common success status codes include (but are not limited to):
* **200 OK**: Standard response for successful HTTP requests. The actual response will depend on the request method used.
* **201 Created**: The request has been fulfilled, resulting in the creation of a new resource.

#### 300s - Additional Steps
This class of status code indicates the client must take additional action to complete the request. Many of these status codes are used in URL redirection.

#### 400s - Client-side Error
This class of status code is intended for situations in which the error seems to have been caused by the client. Some common 400 status codes are:
* **400 Bad Request**: The server cannot or will not process the request due to an apparent client error (bad request syntax, size too large, invalid request message framing, or deceptive request routing)
* **401 Unauthorized**: For use when authentication is required and has failed or has not yet been provided
* **403 Forbidden**: The request contained valid data and was understood by the server, but the server is refusing action. This may be due to the user not having the necessary permissions for a resource or needing an account of some sort, or attempting a prohibited action.
* **404 Not Found**: The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible.

#### 500s - Server-side Error
Response status codes beginning with the digit "5" indicate cases in which the server is aware that it has encountered an error or is otherwise incapable of performing the request.

### Slide 14: POST Request 
```http
POST /api/users HTTP/1.1
Host: example.com
Content-Type: application/json

{
    "username": "newuser",
    "email": "newuser@example.com",
    "password": "securepassword"
}
```

Identify the key components:
1. Request Line
   * Method: `POST`
   * URL: `/api/users`
   * HTTP Version: `HTTP/1.1`
2. Headers
   * Header 1: `Host: example.com`
   * Header 2: `Content-Type: application/json`
3. Blank Line
4. Body
   * JSON Form:
   ```json
   {
       "username": "newuser",
       "email": "newuser@example.com",
       "password": "securepassword"
   }
   ```

### Slide 15: POST Response
```http
HTTP/1.1 201 Created
Content-Type: application/json

{
    "id": 123,
    "username": "newuser",
    "email": "newuser@example.com"
}
```

Identify the key components:
1. Status Line
   * HTTP Version: `HTTP/1.1`
   * Status Code: `201`
   * Status Text: `Created`
2. Headers
   * Header 1: `Content-Type: application/json`
3. Blank Line
4. Body
   * JSON Form:
   ```
   {
       "id": 123,
       "username": "newuser",
       "email": "newuser@example.com"
   }
   ```

### Slide 16: GET Request
```http
GET /api/users?username=newuser HTTP/1.1
Host: example.com
```

Identify the key components:
1. Request Line
   * Method: `GET`
   * URL: `/api/users`
   * Query Parameters: `?username=newuser`
   * HTTP Version: `HTTP/1.1`
2. Headers
   * Header 1: `Host: example.com`

❗ **Important**: We cannot include a body in a GET request so if we need to specify additional information, we do so through the use of query parameters included in the URL.

### Slide 17: GET Response
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "id": 123,
    "username": "newuser",
    "email": "newuser@example.com",
    "bio": "User's biography"
}
```

Identify the key components:
1. Status Line
   * HTTP Version: `HTTP/1.1`
   * Status Code: `200`
   * Status Text: `OK`
2. Headers
   * Header 1: `Content-Type: application/json`
3. Blank Line
4. Body
   * JSON Form:
   ```
   {
       "id": 123,
       "username": "newuser",
       "email": "newuser@example.com",
       "bio": "User's biography"
   }
   ```

### Slide 18: PATCH Request
```http
PATCH /api/users/123 HTTP/1.1
Host: example.com
Content-Type: application/json

{
    "bio": "Updated bio"
}
```

Identify the key components:
1. Request Line
   * Method: `PATCH`
   * URL: `/api/users/123`
   * HTTP Version: `HTTP/1.1`
2. Headers
   * Header 1: `Host: example.com`
   * Header 2: `Content-Type: application/json`
3. Blank Line
4. Body
   * JSON Form:
   ```json
   {
       "bio": "Updated bio"
   }
   ```

### Slide 19: PATCH Response
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "id": 123,
    "username": "existinguser",
    "email": "existinguser@example.com",
    "bio": "Updated bio"
}
```

Identify the key components:
1. Status Line
   * HTTP Version: `HTTP/1.1`
   * Status Code: `200`
   * Status Text: `OK`
2. Headers
   * Header 1: `Content-Type: application/json`
3. Blank Line
4. Body
   * JSON Form:
   ```
   {
       "id": 123,
       "username": "existinguser",
       "email": "existinguser@example.com",
       "bio": "Updated bio"
   }
   ```

### Slide 20: DELETE Request
```http
DELETE /api/users/123 HTTP/1.1
Host: example.com
```

Identify the key components:
1. Request Line
   * Method: `DELETE`
   * URL: `/api/users/123`
   * HTTP Version: `HTTP/1.1`
2. Headers
   * Header 1: `Host: example.com`

❗ **Important**: As with GET requests, we cannot include a body for DELETE requests.

### Slide 21: DELETE Response
```http
HTTP/1.1 204 No Content
```

Identify the key components:
1. Status Line
   * HTTP Version: `HTTP/1.1`
   * Status Code: `204`
   * Status Text: `No Content`
   
## Break (10 minutes)

## Subsection 5: [Hands-On: Making API Requests](https://github.com/rogers-obrien-rad/api-alchemy/blob/main/documents/session1/s1_agenda.md#hands-on-making-api-requests-45-minutes)
