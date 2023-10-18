# Session 2: Working with API Data and API Documentation 📜
_Delve deeper into handling and manipulating data obtained from APIs, understanding different data formats, and exploring how to use and read API documentation effectively._

📹 [Link to Presentation](https://www.beautiful.ai/player/-NcT8oMgP1-HCOsKJEM0)

### Slide 1: Title

### Slide 2: Agenda

## 👨‍🏫 Session 1 Review
<details><summary>Click to Expand</summary>
<hr>

### Slide 4: Previous Topics
_A mini-agenda to review topics from the previous session_
![API Alchemy_ Session 2 (1) - 2023-10-18 07 47 30Part-4-1](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/3b7722f3-7a3a-4768-b886-56a364973d9c)

* What are APIs?
* API Architecture
* HTTP

### ❔ What does API stand for?

### Slide 6: Definition of APIs
_Overview of what an API is with examples_
![API Alchemy_ Session 2 (1) - 2023-10-18 07 47 30Part-6-1](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/ddcd63e5-4c68-47f6-9db7-f4558ccdd450)

> An Application Programming Interface is a set of protocols that allows different software applications to communicate, interact, and share data with each other.
* Watch [video](https://www.youtube.com/watch?v=s7wmiS2mSXY) for good, simple explanation
* Additional examples of APIs
  * **Weather Apps**: Weather apps use APIs to access real-time weather data from external sources. These APIs provide accurate and up-to-date information. By leveraging APIs, weather apps avoid the need to collect and maintain their own weather data.
  * **Social Media**: When you click "Share", an API is invoked, sending the data to the respective social media platform. The platform's API processes the request, posts the content, and provides feedback to the user.
  * **Payment Apps**: When you initiate a payment, the app sends transaction details to the payment gateway's API. The API handles payment authorization, processes the transaction, and returns a response to the app
 
### ❔ What does API stand for?

### Slide 8: Case Studies
![API Alchemy_ Session 2 (1) - 2023-10-18 07 47 30Part-8-1](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/8504e9a2-25b9-4078-88ff-1fec126a83ac)

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

### ❔ What are the two main types of API architecture?

### Slide 10: API Architecture
_How the rules of an API are setup to ensure smooth communication_
![API Alchemy_ Session 2 (1) - 2023-10-18 07 47 30Part-10-1](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/8c6020ca-db05-4833-b385-4fcffdd24727)

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

### Slide 11: Process Overview
_How the API process actually works_
![API Alchemy_ Session 2 (1) - 2023-10-18 07 47 30Part-11-1](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/592bb955-8db6-46a9-a026-4ac493955f55)

1. Client (that is you) makes a request using HTTP
2. Server (that is the program you are accessing) processes the requests, performing the action that you specify (if it can)
3. Response is generated in HTTP and sent back to you, the Client
4. Client processes the response

### Slide 12: HTTP Structure

#### Start Line
_First line of the request/response_
![API Alchemy_ Session 2 (1) - 2023-10-18 07 47 30Part-12-1](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/24f898f7-be2e-495f-98db-6bc851072e36)

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

### ❔ What are some of the common HTTP methods?

### Slide 14: HTTP Methods
_The data manipulation methods used by APIs_
![API Alchemy_ Session 2 (1) - 2023-10-18 07 47 30Part-14-1](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/d360a2eb-e390-4ae4-be0d-a4e1cf9dad07)

There are [9 HTTP methods in HTTP v1.1](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods), but there are four/five ones that are commonly used:
* **POST**: Used to send data to the server, for example, customer information, file upload, etc.
* **GET**: Used to retrieve information from the given server using a given URI. Requests using GET should only retrieve data and should have no other effect on the data.
* **PUT**: Replaces all current representations of the target resource with the uploaded content.
* **PATCH**: Applies partial modifications to a resource.
* **DELETE**: Removes the specified resource.

### Slide 15: POST Request 
![API Alchemy_ Session 2 (1) - 2023-10-18 07 47 30Part-15-1](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/13fe575b-7efa-4df9-81e2-0dc1f2fd4eef)

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

### Slide 16: POST Response
![API Alchemy_ Session 2 (1) - 2023-10-18 07 47 30Part-16-1](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/6bdc5519-d3f8-497b-bb58-6a01d9c2bf77)

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

### Slide 17: Response Status Codes
_Status of the HTTP request_
![API Alchemy_ Session 2 (1) - 2023-10-18 07 47 30Part-17-1](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/9be73357-47ba-4283-bff7-f0ec3871868a)

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

<hr>
</details>

## ℹ️ API Data Formats and Handling Responses
<details><summary>Click to Expand</summary>
<hr>

### ❔ What are the two msot common API data formats?

### Slide 20: XML
_What is XML and what are some key characteristics_
![API Alchemy_ Session 2 (1) - 2023-10-18 07 47 30Part-20-1](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/fbd58507-2405-4f02-a747-826f7a6fa0b9)

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

### Slide 21: XML Example
![API Alchemy_ Session 2 (1) - 2023-10-18 07 47 30Part-21-1](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/b82331ff-00a3-4e38-92b5-a8cf77294a1f)

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

### Slide 22: JSON Data
_What is JSON and what are some key characteristics_
![API Alchemy_ Session 2 (1) - 2023-10-18 07 47 30Part-22-1](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/086fb6d4-2e31-429d-9dc0-06d2a541f808)

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

### Slide 23: JSON Example
![API Alchemy_ Session 2 (1) - 2023-10-18 07 47 30Part-23-1](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/2028fe76-6d55-4dd1-95c3-e8cd4e763d3d)

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

### 🔑 Key Points (Slide 24)
![API Alchemy_ Session 2 (1) - 2023-10-18 07 47 30Part-24-1](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/9edaf0ba-66ba-4efc-8a9f-7cbc9293fe1a)

1. **XML (eXtensible Markup Language)**:
   * XML is a human-readable and machine-readable markup language that structures data in a standardized way, commonly used in APIs.
   * XML offers flexibility through custom tags and structures, with data organized using tags, attributes, and a hierarchical tree structure.
2. JSON (JavaScript Object Notation)
   * JSON is a lightweight data interchange format that is efficient for data exchange, especially between different software systems.
   * JSON represents data using key-value pairs and has a simpler syntax compared to XML, making it easier to use.

<hr>
</details>

## 🔐 API Access and Security
<details><summary>Click to Expand</summary>
<hr>

### Slide 26: Authentication versus Authorization
_Differences between the widely interchanged words_
![API Alchemy_ Session 2 (1) - 2023-10-18 07 47 30Part-26-1](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/0374138c-eef4-4d38-a2fe-2076c49729b0)

#### Authentication
Authentication is the process of verifying the identity of a user, system, or entity. It ensures that the person or entity claiming access to a system or resource is indeed who they say they are. Authentication is the first step in the security process and is typically based on providing credentials such as a username and password, a security token, a fingerprint, or other forms of identity verification. Once authenticated, a user gains access to a system or application.

#### Authorization
Authorization, on the other hand, comes after authentication and involves granting or denying access to specific resources or actions based on the authenticated user's permissions. In essence, authorization determines what actions a user or entity is allowed to perform within a system or application. Authorization is typically defined by roles, permissions, or access levels that are associated with the authenticated user. It ensures that users only have access to the functionalities and data they are entitled to based on their roles or privileges.

#### TL;DR
* **Authentication** is about confirming the identity of a user.
* **Authorization** is about granting or denying access to specific resources or actions based on the user's verified identity and permissions

### Slide 27: Common Authentication Methods
![API Alchemy_ Session 2 (1) - 2023-10-18 07 47 30Part-27-1](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/be45479b-70c3-4629-a55f-5be5ad74cd6e)

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

### Slide 28: Basic Authentication
_Standard username and password_
![API Alchemy_ Session 2 (1) - 2023-10-18 07 47 30Part-28-1](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/e2885124-9337-4ad8-b340-5d73bcdd3f79)

A developer accessing a private GitHub repository using the Git command-line tool. The tool prompts for a username and password, which the developer provides. The credentials are then base64-encoded and included in the Git request headers for authentication.

```bash
git clone https://github.com/username/repo.git
Username: your_username
Password: your_password
```

### Slide 29: API Keys
_Keys provided in header or query parameters_
![API Alchemy_ Session 2 (1) - 2023-10-18 07 47 30Part-29-1](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/e10b6e53-bc4b-41ce-bda8-4708aa7a45b4)

Using a weather API to fetch weather information for your application. The API provider gives you a unique API key. To authenticate, you include the API key in the request URL when making API calls.

```http
GET https://api.weather.com/forecast?api_key=your_api_key
```

### Slide 30: Token-based
_Similar to keys but token expires_
![API Alchemy_ Session 2 (1) - 2023-10-18 07 47 30Part-30-1](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/829fa1a9-e2c6-4734-b6ec-91c458947664)

A mobile app that interacts with a user's social media account. After the user logs in, the app receives a JWT (JSON Web Token). When making requests to the social media API, the app includes the JWT in the request headers.

```http
GET https://api.socialmedia.com/posts
Authorization: Bearer your_jwt
```

### 🔑 Key Points (Slide 31)
_Summary of the API Access and Security section_
![API Alchemy_ Session 2 (1) - 2023-10-18 07 47 30Part-31-1](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/4dc37120-e878-40ca-b3f5-407eb0d2b225)

1. **Authentication vs. Authorization**: Authentication is the process of verifying a user's identity (e.g., through username/password), while authorization determines the access or actions a user can perform based on their permissions.
2. **API Keys**: Simple alphanumeric strings given by API providers to authenticate clients. Often used for public APIs with lower security requirements and can be passed in headers or query parameters.
3. **Bearer Token Authentication**: Uses tokens, like JWT or OAuth 2.0 access tokens. Upon successful authentication, clients receive an access token to include in request headers, offering flexibility and scalability.
4. **Basic Authentication**: Involves sending base64-encoded usernames and passwords in request headers. It's simple but less secure due to potential interception risks.

<hr>
</details>

## 📝 API Documentation
<details><summary>Click to Expand</summary>
<hr>

### Slide 33: Navigating Docs
_A guidebook to the API's capabilities and usage_
![API Alchemy_ Session 2 (1) - 2023-10-18 07 47 30Part-33-1](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/c92fab13-1c51-46c6-8010-a3f00099948a)

Key components of API documentation include:
* **Endpoints**: These are URLs that define specific functions or resources the API provides.
* **Parameters**: These are inputs required to customize your API requests, such as query parameters, headers, or request bodies.
* **Responses**: Documentation explains what data the API returns in response to different requests.
* **Authentication**: Details about how to authenticate and authorize your requests using API keys, tokens, or other methods.

Some examples:
* [Procore API Docs](https://developers.procore.com/reference/rest/v1/docs/rest-api-overview)
* [OpenWeatherMap API Docs](https://openweathermap.org/current#concept)
* [NASA API Docs](https://ssd-api.jpl.nasa.gov/doc/index.php)

### Slide 34: Endpoints
_More details on endpoints_
![API Alchemy_ Session 2 (1) - 2023-10-18 07 47 30Part-34-1](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/9f02e971-3c8b-47c0-8fd9-ee4ee10d8d2a)

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

### Slide 35: Parameters
_The three types of parematers and what their usage is_
![API Alchemy_ Session 2 (1) - 2023-10-18 07 47 30Part-35-1](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/fa381942-e317-4f92-aefe-08905732418e)

#### Header Parameters
* **Purpose**: Header parameters contain additional information about the request or the client making the request.
* **Usage**: Header parameters are included in the headers section of the HTTP request. They provide context or instructions for the server to process the request properly. Examples include authentication tokens, user agents, and content types (e.g., JSON or XML).

#### Path Parameters
* **Purpose**: Path parameters allow dynamic segments in the URL path to identify specific resources or actions.
* **Usage**: Path parameters are inserted directly into the URL path and enclosed within curly braces. They are used to specify identifiers, such as IDs or slugs, that help the server determine which resource the client is requesting. For instance, in a URL like `/users/{user_id}`, `user_id` is a path parameter.

#### Query Parameters
* **Purpose**: Query parameters enable customization and filtering of API requests by providing additional information to the server.
* **Usage**: Query parameters are appended to the URL after a question mark (?). They are in the form of key-value pairs, separated by &. Query parameters help modify the behavior of the request, such as specifying search terms, filters, sorting options, or pagination limits. For example, in a URL like `/products?category=electronics&sort=price`, `category` and `sort` are query parameters.

### Slide 36: Parameters Example
_How parameters are documented_
![API Alchemy_ Session 2 (1) - 2023-10-18 07 47 30Part-36-1](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/d40dc0bf-5e6f-4d60-85af-55e200948f6e)

#### Documentation for Path Parameters typically includes:
* **Names**: Documentation lists the names of path parameters that you may need to include in your API request's URL.
* **Types**: The data types or formats expected for each path parameter. This information helps you ensure that your parameter values match the expected type.
* **Placement**: Path parameters are typically included directly in the URL's path, and the documentation shows where in the URL to place each parameter.
* **Constraints**: Documentation may outline any constraints or validation rules that path parameters must adhere to, such as minimum/maximum lengths or allowed characters.
* **Required Parameters**: Whether a path parameter is required or optional. If a parameter is required, it must be included in the URL for the request to be valid.
* **Example URLs**: Documentation often provides examples of complete URLs with path parameters included. These examples serve as templates for constructing your requests.
* **Descriptions**: You'll find descriptions or explanations for each path parameter, helping you understand its purpose and usage within the API request.

#### Documentation for Query Parameters typically includes:
* **Names**: Documentation lists the names of query parameters that you may include in your API request's URL. These parameters are typically added after the "?" character in the URL.
* **Types**: It specifies the data types or formats expected for each query parameter, helping you ensure that your parameter values match the expected type.
* **Usage**: Query parameters are typically used to filter, paginate, or customize API responses. Documentation explains how each parameter affects the response.
* **Constraints**: Documentation may outline any constraints or validation rules that query parameters must adhere to, such as valid values or numeric ranges.
* **Optional Parameters**: Query parameters are often optional, meaning you can choose whether to include them in the URL. Documentation indicates which parameters are optional and which are required.
* **Example URLs**: Documentation provides examples of complete URLs with query parameters included, showing how to structure requests for specific use cases.
* **Parameter Descriptions**: You'll find descriptions or explanations for each query parameter, helping you understand its purpose and how it influences the API response.

#### Documentation for Headers typically includes:
* **Names**: Documentation lists the names of the headers that you may need to include in your API request. These names are case-sensitive and should be entered exactly as specified.
* **Values**: For each header, it specifies the expected or allowed values. Some headers may have specific values that are required or optional.
* **Examples**: Documentation often provides examples of header configurations for different scenarios.
* **Header Descriptions**: You'll find descriptions or explanations for each header, clarifying its purpose and how it affects the API request or response.
* **Required Headers**: It specifies whether a header is required or optional. If a header is required, it's crucial to include it in your request; otherwise, the request may fail.
* **Format**: Information about the format or syntax of headers is given. For instance, some headers require a specific format, like date and time in a specific format.
* **Authentication Headers**: If the API uses authentication, the documentation provides details about headers required for authentication, such as API keys or tokens.

Below is the [Procore API Documentation](https://developers.procore.com/reference/rest/v1/rfis?version=1.0#create-rfi) on how to create a RFI using a POST request:

![image](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/130a98cc-9722-4dc6-a86c-9614883f6733)

You can see we have:
* **Header Parameter**: `Procore-Company-Id` which needs to be an integer
* **Path Parameter**: `project_id` which also needs to be an integer
* **Query Parameter**: `run_configurable_validations` which is a boolean

The actual request in HTTP might look something like this:

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

Where:
* **Header Parameters**: All parameters under the URL such as `Authorization` and `Content-Type`
* **Path Parameter**: `681425` is placed in the URL
* **Query Parameter**: `run_configurable_validation` is placed after the question mark "?"

### Slide 37: Request Body
_How documentation specifies the request body_
![API Alchemy_ Session 2 (1) - 2023-10-18 07 47 30Part-37-1](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/e54dc335-e35a-470a-8920-1da55cb4ced2)

API documentation typically displays request body notes by providing detailed information on how to structure and format the data that you need to send in the request body when making an API call. These notes may include:
* **Data Format**: Documentation explains the expected data format, which can be JSON, XML, form data, or another format.
* **Parameters**: It lists the parameters or fields that should be included in the request body. Each parameter is described, including its name, type, and whether it's required.
* **Example**: Documentation often provides an example request body, showing you exactly how the data should be structured.
* **Data Types**: It clarifies the data types allowed for each parameter (e.g., string, number, boolean) and may specify any constraints or validation rules.
* **Validation Rules**: Documentation may detail any specific validation rules or patterns that the data must adhere to, such as minimum/maximum lengths or allowed characters.
* **Default Values**: If some parameters have default values, those values are usually documented.
* **Notes and Descriptions**: You may find explanations or descriptions of each parameter, helping you understand their purpose and usage.

Below is a screenshot taken from the [Procore API Documentation](https://developers.procore.com/reference/rest/v1/project-folders-and-files?version=1.0#create-project-folder) on how to create a folder in Procore using a POST request:
![image](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/df1ac7d7-1323-4617-9a5b-ff72564ed5ee)

The actual JSON data that you would send in the body would look something like this:

```json
{
  "folder": {
    "parent_id": 12,
    "name": "test_folder",
    "is_tracked": true,
    "explicit_permissions": true,
    "custom_field_%{custom_field_definition_id}": "string"
  }
}
```

### Slide 38: Responses
_Example responses bodies and status codes_
![API Alchemy_ Session 2 (1) - 2023-10-18 07 47 30Part-38-1](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/fb794822-32e7-4b52-bb6c-3dac6bd093c1)

Documentation typically contains:
* **Status Codes**: Documentation lists common HTTP status codes that the API request can return.
* **Response Descriptions**: For each status code, documentation provides a description of what it means in the context of the API.
* **Example Responses**: Documentation may include sample API responses for each status code. These examples show the structure and content of the response body that you can expect to receive in different scenarios.
* **Response Formats**: Information about the response format, such as JSON or XML, is usually provided alongside the examples to ensure developers know how to parse and work with the response data.

![image](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/b2b9c88c-43eb-41af-aa13-b2eb7bf7bbb0)

Some documenation, like for [Procore's API](https://developers.procore.com/reference/rest/v1/project-folders-and-files?version=1.0#create-project-file), include the response by status code which can be helpful to debug issues. 

### Slide 39: Authentication
_How to manage authentication for your requests_
![API Alchemy_ Session 2 (1) - 2023-10-18 07 47 30Part-39-1](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/ad18a6fd-e028-4b50-a5d6-f8d843a59dc8)

In API documentation, authentication is a crucial topic covered to guide developers on how to securely access the API. Here's how authentication is typically addressed in API documentation
* **Authentication Methods**: API documentation explains the available authentication methods, such as API keys, OAuth tokens, JWT (JSON Web Tokens), or basic authentication.
* **Authentication Endpoints**: For APIs using OAuth or token-based authentication, documentation provides information on the authentication endpoints, where developers can obtain the necessary tokens or keys.
* **Authentication Parameters**: Documentation specifies the required authentication parameters that must be included in API requests, such as API keys, tokens, or credentials. It details where to place these parameters, whether in headers, query parameters, or request bodies.
* **Example Authentication**: To demonstrate the authentication process, API documentation often includes step-by-step examples of how to obtain authentication credentials and use them in API requests.
* **Rate Limiting**: Some API documentation may mention rate limiting, which restricts the number of requests a client can make within a certain time frame. 
* **Token Refresh**: If applicable, documentation explains how to refresh authentication tokens and manage token expiration.
* **Error Handling**: Documentation provides information on error responses related to authentication, helping developers troubleshoot authentication issues.

You can view the authentication documentation for a few APIs:
* [Procore](https://developers.procore.com/reference/rest/v1/docs/making-first-call)
* [GitHub](https://docs.github.com/en/rest/guides/getting-started-with-the-rest-api?apiVersion=2022-11-28)
* [NASA](https://api.nasa.gov/)

<hr>
</details>
   
## Break (10 minutes)

## 👐Hands-On: Making API Requests
<details><summary>Click to Expand</summary>
<hr>

### Slide 41: Hands-On Agenda
During the Hands-On Session we will be:
1. Learning how to extract data from responses systematically
2. Use the Procore API

### 🏆 Challenge: Making a GET Request
Use the [PokeAPI](https://pokeapi.co/) in Postman to make a request to get data on your favorite Pokemon!
1. Navigate to the [PokeAPI](https://pokeapi.co/docs/v2 ) documentation and find the endpoint that gives you the overall information on a Pokemon
2. Craft the GET request in [Postman](www.postman.com)
3. Be the first to do so and win a prize!

### Slide 43: Using Reponse Data in Postman
Use the links below to find more information:
* For RO: [Playbook](https://app.getguru.com/folders/Tqbx9ygc/Procore-API?activeCard=231f1661-2254-403b-b5af-cf29a4673a02)

### Slide 44: Using Reponse Data in Postman
Use the links below to find more information:
* For RO: [Playbook](https://app.getguru.com/folders/Tqbx9ygc/Procore-API?activeCard=952225df-921e-4fea-b22d-f283a37be009)

### Slide 45: Using Reponse Data in Postman
Use the links below to find more information:
* For RO: [Playbook](https://app.getguru.com/folders/Tqbx9ygc/Procore-API?activeCard=335584a3-b7e4-4ab1-841b-8651ec8e5df5)

### Slide 46: Using Reponse Data in Postman
Use the links below to find more information:
* For RO: [Playbook](https://app.getguru.com/folders/Tqbx9ygc/Procore-API?activeCard=a0d189d5-1a15-4f5a-b360-abade464150e)

<hr>
</details>
