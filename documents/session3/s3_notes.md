# Session 3: Using Python for API Calls and Data Manipulation 🐍
_Leveling up from Postman to Python_

📹 [Link to Presentation](https://www.beautiful.ai/-Nd6mf12-F_Jh78lUfQM/8)

## Subsection 1: [Session 2 Review](https://github.com/rogers-obrien-rad/api-alchemy/blob/main/documents/session2/s2_agenda.md#session-1-review-10-minutes)

### Slide 1: Title

### Slide 2: Agenda

## 👨‍🏫 Session 2 Review
<details><summary>Click to Expand</summary>
<hr>

### Slide 4: Previous Topics

1. **API Data Formats**: XML (boo) and JSON (yay)
2. **API Access**: Authorization and Authentication methods
3. **Documentation**: Setup and understanding request formats

### ❔ What does JSON stand for?

### Slide 6: JSON Data
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

#### JSON Example

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

### ❔ What is the difference between Authentication and Authorization?

### Slide 8: Authentication versus Authorization
_Differences between the widely interchanged words_

#### Authentication
Authentication is the process of verifying the identity of a user, system, or entity. It ensures that the person or entity claiming access to a system or resource is indeed who they say they are. Authentication is the first step in the security process and is typically based on providing credentials such as a username and password, a security token, a fingerprint, or other forms of identity verification. Once authenticated, a user gains access to a system or application.

#### Authorization
Authorization, on the other hand, comes after authentication and involves granting or denying access to specific resources or actions based on the authenticated user's permissions. In essence, authorization determines what actions a user or entity is allowed to perform within a system or application. Authorization is typically defined by roles, permissions, or access levels that are associated with the authenticated user. It ensures that users only have access to the functionalities and data they are entitled to based on their roles or privileges.

#### TL;DR
* **Authentication** is about confirming the identity of a user.
* **Authorization** is about granting or denying access to specific resources or actions based on the user's verified identity and permissions

### ❔ What are some common authentication methods?

### Slide 10: Common Authentication Methods

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

### Slide 11: API Documentation
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

<hr>
</details>

## 👐 Hands-On: Making API Requests
<details><summary>Click to Expand</summary>
<hr>

### Slide 13: Getting Started
_Get Python up and everything else you need_

1. Install Python
   * Naturally you will need this program to run Python scripts!
   * [Playbook Article](https://app.getguru.com/folders/T9b9aGnc/Python?activeCard=b840ce1b-208b-4765-8a95-b7902b260c84)
2. Install Visual Studio Code
   * A nice environment to code in with a lot of features and plug-ins (including AI tools!)
   * [Playbook Article](https://app.getguru.com/folders/T9b9aGnc/Python?activeCard=b840ce1b-208b-4765-8a95-b7902b260c84) - same article as above, just look in different section!
  
### Slide 15: Introduction to Python

### Slide 16: Basic Outputs
The print function in Python is used to display text or variable values in the console.
```python
print("Hello, World!")
```

### Slide 17: Variables

#### Variables Types
Variables act as placeholders to store data values in memory. Different data types can be assigned to variables such as:
* String: Textual data
``` python
name = "Hagen"
```
* Integer: Whole numbers
```python
age = 29
```
* Float: Decimal numbers
``` python
height = 6.0
```
* Boolean: binary true or false (0 or 1)
```python
works_at_ro = True
```

> Unlike other languages, Python does not require you to declare the type of variable when declaring it. Python will figure out the variable type for you when you run your code. 

#### Variable Naming
* **Starting Character**: Variable names must start with a letter (a-z, A-Z) or an underscore (_). The rest of the name can contain letters, numbers, or underscores.
* **Case-Sensitive**: Variable names are case-sensitive (age, Age, and AGE are three different variables).
* **Reserved Words**: Python has defined keywords like `if`, `else`, `while`, etc.) that cannot be used as variable names.

Slide 18: ### Lists
Lists are ordered collections of items, and they can hold any type of data.
```python
fruits = ["apple", "banana", "cherry"]
```

Items in lists can be accessed by their index, with indices starting from 0 for the first item.
```
print(fruits[0])
```

### Slide 19: Dictionaries
Dictionaries in Python store data in key-value pairs and look very similar to JSON-formatted data:
```python
person = {
    "name": "Hagen",
    "age": 29,
    "city": "Austin"
}
```
Values in a dictionary can be accessed using their respective keys:
```python
print(person["name"]) # Hagen
print(person["age"]) # 29
```

### Slide 20: Advanced Outputs: F-Strings (Formatted String Literals)
Introduced in Python 3.6, f-strings offer a concise way to embed expressions inside string literals. They are prefixed with an 'f' and use curly braces {} to embed Python expressions within the string.

```python
name = "John"
age = 25
greeting = f"My name is {name} and I am {age} years old."
print(greeting)  # Output: My name is John and I am 25 years old.
```

You can also perform operations within the curly braces of an f-string.

```python
double_age = f"Twice my age is {age * 2}."
print(double_age)  # Output: Twice my age is 50.
```

F-strings provide a readable and convenient way to include variable values and expressions directly within strings, making code cleaner and more intuitive.

### Slide 21: Conditionals
Conditionals allow for the execution of a block of code only if a specified condition is met.
```python
if age > 18:
    print("John is an adult.")
else:
    print("John is not an adult.")
```

### Slide 22: Loops
Loops in Python are used to execute a block of code multiple times.

* for loop: Iterates through a list or range.
```python
for fruit in fruits:
    print(fruit)
```

* while loop: Executes as long as a specified condition remains true.
```python
count = 0
while count < 3:
    print(f"Count is: {count}")
    count += 1
``` 

### Slide 23: Functions
* **Definition**: Functions are blocks of organized and reusable code designed to perform a specific task. They are a fundamental concept in programming, allowing for modularity and code reuse.
```python
def function_name(parameters):
    """docstring: provides a brief explanation of what the function does, the input(s), and the output(s)"""
    # function body
    return output
```
* **Parameters and Arguments**
    * Parameters are the names listed in the function's definition.
    * Arguments are the real values passed to the function when it's called.
```python
def greet(person_name):
    message = f"Hello, {person_name}!"
    return message
```
* **Return Statement**: The return keyword is used to exit a function and return a value.

```python
def add(x, y):
    return x + y
```

* **Variable Scope**
    * Local Variables: Variables declared inside a function have a local scope, meaning they can only be accessed within that function
    * Global Variables:  Variables declared outside of the function (or in global scope) can be accessed inside or outside of the function
 
```python
x = 10  # This is a global variable

def check_value():
    y = 5  # This is a local variable
    return x + y  # Can access global variable 'x' inside this function
```

### Slide 24: Package Imports
In Python, we can enhance the default capabilities by importing external packages. This is done using the import keyword. In the script, two packages are imported:

* requests: Used for making HTTP requests.
```python
import requests
```
* pandas (often imported as pd): Used for data manipulation and analysis.
```python
import pandas as pd
```

<hr>
</details> 
   
## Break (10 minutes)

## 👐 Hands-On: Making API Requests
<details><summary>Click to Expand</summary>
<hr>

### Slide 25: Python `requests` Library

### Slide 26: GET Request

### Slide 27: Check Status Code

### Slide 28: Check Response Content



### Slide 30: Hands-On Agenda
During the Hands-On Session we will be:
1. Learning how to extract data from responses systematically
2. Use the Procore API

### Slide 31: Using Reponse Data in Postman
Use the links below to find more information:
* For RO: [Playbook](https://app.getguru.com/folders/izbexgGT/Postman-API-Testing?activeCard=15175606-2fee-4929-8d2c-8e6a699d3ecc)
* For OthersL [GitHub](https://github.com/rogers-obrien-rad/api-alchemy/blob/main/documents/postman/8_using_response_data.md)

### Slide 32: Using Reponse Data in Postman
Use the links below to find more information:
* For RO: [Playbook](https://app.getguru.com/folders/Tqbx9ygc/Procore-API?activeCard=231f1661-2254-403b-b5af-cf29a4673a02)

### Slide 33: Using Reponse Data in Postman
Use the links below to find more information:
* For RO: [Playbook](https://app.getguru.com/folders/Tqbx9ygc/Procore-API?activeCard=952225df-921e-4fea-b22d-f283a37be009)

### Slide 34: Using Reponse Data in Postman
Use the links below to find more information:
* For RO: [Playbook](https://app.getguru.com/folders/Tqbx9ygc/Procore-API?activeCard=335584a3-b7e4-4ab1-841b-8651ec8e5df5)

### Slide 35: Using Reponse Data in Postman
Use the links below to find more information:
* For RO: [Playbook](https://app.getguru.com/folders/Tqbx9ygc/Procore-API?activeCard=a0d189d5-1a15-4f5a-b360-abade464150e)

<hr>
</details>
