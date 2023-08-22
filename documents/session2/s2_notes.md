Session 2: Working with API Data and API Documentation 📜
_Delve deeper into handling and manipulating data obtained from APIs, understanding different data formats, and exploring how to use and read API documentation effectively._

## Subsection 1: [Session 1 Review](https://github.com/rogers-obrien-rad/api-alchemy/blob/main/documents/session2/s2_agenda.md#session-1-review-10-minutes)

### Slide 1: Title

### Slide 2: Agenda

### Slide 3: Previous Topics
_A mini-agenda to review topics from the previous session_
* What are APIs?
* API Architecture
* HTTP

### Slide 4: Definition of APIs
_Overview of what an API is with examples_

> An Application Programming Interface is a set of protocols that allows different software applications to communicate, interact, and share data with each other.
* Watch [video](https://www.youtube.com/watch?v=s7wmiS2mSXY) for good, simple explanation
* Additional examples of APIs
  * **Weather Apps**: Weather apps use APIs to access real-time weather data from external sources. These APIs provide accurate and up-to-date information. By leveraging APIs, weather apps avoid the need to collect and maintain their own weather data.
  * **Social Media**: When you click "Share", an API is invoked, sending the data to the respective social media platform. The platform's API processes the request, posts the content, and provides feedback to the user.
  * **Payment Apps**: When you initiate a payment, the app sends transaction details to the payment gateway's API. The API handles payment authorization, processes the transaction, and returns a response to the app

### Slide 5: Case Studies

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

### Slide 6: API Architecture
_How the rules of an API are setup to ensure smooth communication_

#### SOAP (Simple Object Access Protocol):
* Like sending a package with instructions and details
* More structured and formal than REST
* Often used in big businesses
* Communication is more like writing a letter: you need to follow specific rules
* Can use different delivery methods (transport protocols) like HTTP, SMTP (email), etc.
* Has a fixed structure (XML) for messages, making sure everyone understands the message format

#### REST (Representational State Transfer):
* Modern and simple way for software to communicate over the internet
* Communication is like talking to a waiter: you ask for things (GET), give new things (POST), update (PUT), or remove (DELETE)
* Simple and straightforward
* Uses URLs to represent different resources (like menu items), and you use different actions (HTTP methods) to interact with those resources

### Slide 7: Process Overview
_How the API process actually works_
1. Client (that is you) makes a request using HTTP
2. Server (that is the program you are accessing) processes the requests, performing the action that you specify (if it can)
3. Response is generated in HTTP and sent back to you, the Client
4. Client processes the response

### Slide 8: HTTP Structure

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

### Slide 9: HTTP Methods
_The data manipulation methods used by APIs_

There are [9 HTTP methods in HTTP v1.1](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods), but there are four/five ones that are commonly used:
* **POST**: Used to send data to the server, for example, customer information, file upload, etc.
* **GET**: Used to retrieve information from the given server using a given URI. Requests using GET should only retrieve data and should have no other effect on the data.
* **PUT**: Replaces all current representations of the target resource with the uploaded content.
* **PATCH**: Applies partial modifications to a resource.
* **DELETE**: Removes the specified resource.

### Slide 10: POST Request 
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

### Slide 11: POST Response
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

### Slide 12: Response Status Codes
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
   
## Break (10 minutes)

## Subsection 5: [Hands-On: Making API Requests](https://github.com/rogers-obrien-rad/api-alchemy/blob/main/documents/session1/s1_agenda.md#hands-on-making-api-requests-45-minutes)
