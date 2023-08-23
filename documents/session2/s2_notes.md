# Session 2: Working with API Data and API Documentation 📜
_Delve deeper into handling and manipulating data obtained from APIs, understanding different data formats, and exploring how to use and read API documentation effectively._

📹 [Link to Presentation](https://www.beautiful.ai/player/-NcT8oMgP1-HCOsKJEM0)

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

## Subsection 2: [API Data Formats and Handling Responses](https://github.com/rogers-obrien-rad/api-alchemy/blob/main/documents/session2/s2_agenda.md#api-data-formats-and-handling-responses-10-minutes)

### Slide 13: XML
_What is XML and what are some key characteristics_

XML (eXtensible Markup Language) is a widely used format for structuring and representing data that needs to be exchanged between different software systems. XML is not limited to APIs; it's also used for data storage, configuration files, and more.
* **Definition**: XML is a markup language that defines rules for encoding documents in a format that is both human-readable and machine-readable.
* **Purpose**: XML is used to structure and represent data in a hierarchical and standardized way, making it easier for different software applications to understand and process the data.

#### XML in API Context:
* **Data Exchange**: APIs often use XML as a format for exchanging data between a client (requester) and a server (provider).
* **Data Representation**: XML allows you to represent structured data with elements, attributes, and values, making it suitable for various types of information like configuration settings, lists, documents, and more.
* **Data Types**: XML supports a wide range of data types, including strings, numbers, dates, and more complex structures.
* **Flexibility**: XML is extensible, meaning you can define custom tags and structures to represent specific data formats or schemas.
* **Human-Readable**: XML documents are designed to be both human-readable and machine-readable. This readability helps developers understand the structure and content of the data being exchanged.

#### XML Structure:
* **Tags**: XML documents use tags to define elements that hold data. Tags are enclosed in angle brackets, like `<tag>`.
* **Attributes**: Elements can have attributes that provide additional information. Attributes are defined within the opening tag, like `<element attribute="value">`.
* **Hierarchy**: XML documents have a hierarchical structure, with elements nested within other elements to create a tree-like arrangement.
* **Closing Tags**: Each opening tag must have a corresponding closing tag (e.g., `<tag>data</tag>`).

### Slide 14: XML Example

```xml
<bookstore>
    <book category="Fiction">
        <title>The Great Gatsby</title>
        <author>F. Scott Fitzgerald</author>
        <price>10.99</price>
    </book>
    <book category="Non-Fiction">
        <title>Sapiens</title>
        <author>Yuval Noah Harari</author>
        <price>15.95</price>
    </book>
</bookstore>
```

### Slide 15: JSON Data
_What is JSON and what are some key characteristics_

JSON (JavaScript Object Notation) is:
* **Definition**: a lightweight data interchange format that is easy for both humans and machines to read and write.
* **Purpose**: used to structure and represent data in a format that is efficient for data exchange between different software systems.

#### JSON in API Context
* **Data Exchange**: APIs often use JSON as a format for exchanging structured data between clients and servers.
* **Data Representation**: JSON represents data as key-value pairs, arrays, and nested objects, making it suitable for various types of information.
* **Data Types**: JSON supports basic data types such as strings, numbers, booleans, arrays, and objects.
* **Simplicity**: JSON's syntax is less verbose than XML, which contributes to its simplicity and ease of use.

#### JSON Structure
* **Objects**: JSON data is organized into objects, which consist of key-value pairs enclosed in curly braces ({}).
* **Arrays**: Arrays in JSON are ordered lists of values enclosed in square brackets ([]).
* **Values**: Values can be strings, numbers, booleans, objects, arrays, or null.
* **Keys**: Keys are strings that represent the names of values within objects.

### Slide 16: JSON Example

```json
{
    "bookstore": {
        "books": [
            {
                "category": "Fiction",
                "title": "The Great Gatsby",
                "author": "F. Scott Fitzgerald",
                "price": 10.99
            },
            {
                "category": "Non-Fiction",
                "title": "Sapiens",
                "author": "Yuval Noah Harari",
                "price": 15.95
            }
        ]
    }
}
```

## Subsection 3: [API Access and Security](https://github.com/rogers-obrien-rad/api-alchemy/blob/main/documents/session2/s2_agenda.md#api-access-and-security-20-minutes)

### Slide 17: Authentication versus Authorization
_Differences between the widely interchanged words_

#### Authentication
Authentication is the process of verifying the identity of a user, system, or entity. It ensures that the person or entity claiming access to a system or resource is indeed who they say they are. Authentication is the first step in the security process and is typically based on providing credentials such as a username and password, a security token, a fingerprint, or other forms of identity verification. Once authenticated, a user gains access to a system or application.

#### Authorization
Authorization, on the other hand, comes after authentication and involves granting or denying access to specific resources or actions based on the authenticated user's permissions. In essence, authorization determines what actions a user or entity is allowed to perform within a system or application. Authorization is typically defined by roles, permissions, or access levels that are associated with the authenticated user. It ensures that users only have access to the functionalities and data they are entitled to based on their roles or privileges.

#### TL;DR
* **Authentication** is about confirming the identity of a user.
* **Authorization** is about granting or denying access to specific resources or actions based on the user's verified identity and permissions

### Slide 18: Common Authentication Methods

#### API Keys
* API keys are simple and widely used for authentication.
* They are unique alphanumeric strings issued to clients (applications or users) by the API provider.
* Clients include the API key in the request headers or query parameters to authenticate themselves.
* API keys are suitable for public APIs with lower security requirements.

#### Bearer Token Authentication (Token-based)
* Bearer token authentication is used with tokens like JWT (JSON Web Token) or OAuth 2.0 access tokens.
* After successful authentication, clients receive an access token, which they include in the request headers.
* The server validates the token to authorize the client's access to resources.
* Bearer token authentication provides flexibility and scalability.

#### Basic Authentication
* Basic Authentication involves sending a username and password in the request headers.
* The credentials are typically base64-encoded (but not encrypted), making it important to use HTTPS for secure transmission.
* While simple to implement, Basic Authentication is less secure due to the risk of credentials being intercepted.

### Slide 19: Basic Authentication
_Standard username and password_

A developer accessing a private GitHub repository using the Git command-line tool. The tool prompts for a username and password, which the developer provides. The credentials are then base64-encoded and included in the Git request headers for authentication.

```bash
git clone https://github.com/username/repo.git
Username: your_username
Password: your_password
```

### Slide 20: API Keys
_Keys provided in header or query parameters_

Using a weather API to fetch weather information for your application. The API provider gives you a unique API key. To authenticate, you include the API key in the request URL when making API calls.

```http
GET https://api.weather.com/forecast?api_key=your_api_key
```

### Slide 21: Token-based
_Similar to keys but token expires_

A mobile app that interacts with a user's social media account. After the user logs in, the app receives a JWT (JSON Web Token). When making requests to the social media API, the app includes the JWT in the request headers.

```http
GET https://api.socialmedia.com/posts
Authorization: Bearer your_jwt
```

## Subsection 4: [API Documentation](https://github.com/rogers-obrien-rad/api-alchemy/blob/main/documents/session2/s2_agenda.md#api-documentation-and-how-to-useread-it-10-minutes)

### Slide 22: Navigating Docs
_A guidebook to the API's capabilities and usage_

Key components of API documentation include:
* **Endpoints**: These are URLs that define specific functions or resources the API provides.
* **Parameters**: These are inputs required to customize your API requests, such as query parameters, headers, or request bodies.
* **Responses**: Documentation explains what data the API returns in response to different requests.
* **Authentication**: Details about how to authenticate and authorize your requests using API keys, tokens, or other methods.

Some examples:
* [Procore API Docs](https://developers.procore.com/reference/rest/v1/docs/rest-api-overview)
* [OpenWeatherMap API Docs](https://openweathermap.org/current#concept)
* [NASA API Docs](https://ssd-api.jpl.nasa.gov/doc/index.php)

### Slide 23: Endpoints
_More details on endpoints_
* **Definition**: Endpoints are specific URLs that represent different functions or resources within an API. Each endpoint corresponds to a particular action or retrieval of data.
* **Purpose**: Endpoints act as the entry points for clients (applications or users) to interact with an API. They provide a structured way to access specific functionalities offered by the API.
* **Usage**: Clients use different HTTP methods (GET, POST, PUT, DELETE, etc.) on specific endpoints to perform actions like retrieving data, creating new records, updating existing records, or deleting data.

#### GET Endpoint for Retrieving User Information:
* **Endpoint**: /api/users/{user_id}
* **Description**: This endpoint is used to retrieve information about a specific user identified by their user_id.
* **HTTP Method**: GET
** Example Request**:
```http
GET /api/users/123
```

#### POST Endpoint for Creating a New Post:
* **Endpoint**: /api/posts
* **Description**: This endpoint allows clients to create a new post.
* **HTTP Method**: POST
* **Example Request**:
```http
POST /api/posts
{
  "title": "New Post Title",
  "content": "This is the content of the new post."
}
```

### Slide 24: Parameters
_The three types of parematers and what their usage is_

#### Header Parameters
* **Purpose**: Header parameters contain additional information about the request or the client making the request.
* **Usage**: Header parameters are included in the headers section of the HTTP request. They provide context or instructions for the server to process the request properly. Examples include authentication tokens, user agents, and content types (e.g., JSON or XML).

#### Path Parameters
* **Purpose**: Path parameters allow dynamic segments in the URL path to identify specific resources or actions.
* **Usage**: Path parameters are inserted directly into the URL path and enclosed within curly braces. They are used to specify identifiers, such as IDs or slugs, that help the server determine which resource the client is requesting. For instance, in a URL like `/users/{user_id}`, `user_id` is a path parameter.

#### Query Parameters
* **Purpose**: Query parameters enable customization and filtering of API requests by providing additional information to the server.
* **Usage**: Query parameters are appended to the URL after a question mark (?). They are in the form of key-value pairs, separated by &. Query parameters help modify the behavior of the request, such as specifying search terms, filters, sorting options, or pagination limits. For example, in a URL like `/products?category=electronics&sort=price`, `category` and `sort` are query parameters.

### Slide 25: Parameters Example
_Highlighting how parameters are used when making an HTTP request_

```http
POST /rest/v1.0/projects/681425/rfis?run_configurable_validations=False HTTP/1.1
Host: api.procore.com
Authorization: Bearer REPLACE_BEARER_TOKEN
Procore-Company-Id: 8089
Content-Type: application/json

{
  "rfi": {
    "subject": "Wall Color",
    "reference": "Color of the kitchen wall"
  }
}
```
   
## Break (10 minutes)

## Subsection 5: [Hands-On: Making API Requests](https://github.com/rogers-obrien-rad/api-alchemy/blob/main/documents/session1/s1_agenda.md#hands-on-making-api-requests-45-minutes)
