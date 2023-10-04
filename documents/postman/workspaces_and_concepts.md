# POSTMAN: WORKSPACES AND CONCEPTS OVERVIEW

## OVERVIEW OF THE WORKSPACE

You will be doing most of your work in the Workspace which is shown below:

![image1](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/1df3421f-dc8d-4fad-a49f-b42a35ebebab)

### EDITOR

In the center of the display will be the editor which allows you to make changes to file or request that you are working on. In the screenshot above, nothing is open. If you click the "+" icon you will create a new tab that defaults to an HTTP request:

![image2](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/bb27d12a-a8d4-4511-b161-7bb2f2ef9e8a)



### SIDEBAR

On the left-hand side you will see the sidebar and 4 icons:

![image3](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/e6583e9c-4cb9-4dff-b35d-4805dbca51d4)


 * Collections: Postman lets users group related API requests into collections, making it easy to organize and manage requests for specific projects or tasks.
 * Environments: Users can create different environments to store variables like API keys, making requests portable and adaptable to different contexts.
 * History: The "History" tab maintains a chronological list of all the API requests you've sent through Postman.

The last icon lets you configure the sidebar to include more tabs or hide the ones that are currently displayed.


### CONSOLE

The console can be shown by finding the button at the bottom-left of the screen. Clicking this button will open up the console which allows us to see the Logs of the requests we have made:

![image4](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/82529449-5129-4ded-9458-f4c27fbc7e51)


## IMPORTANT POSTMAN CONCEPTS AND FEATURES

This section details some of the concepts and features that Postman provides that you should take advantage of when you can.


### COLLECTIONS

"Collections" are a fundamental organizational feature that allow you to group and manage related API requests, making it easier to organize, execute, and share them. Collections serve as containers for storing a set of API requests, typically related to a specific project, API, or functionality. Here are some features of collections:

 1. Easy Organization: Collections can be organized hierarchically. You can create sub-collections within larger collections to further categorize your requests.
 2. Request Order: Within a collection, you can specify the order in which requests should be executed. This is helpful when you have dependencies between requests.
 3. Sharing and Collaboration: Collections can be easily shared with team members or collaborators. This is valuable for ensuring that everyone has access to the same set of requests and can work collaboratively.
 4. Variables and Environments: Collections can utilize variables and environments. This allows you to parameterize your requests, making them adaptable to different environments (e.g., development, testing, production) and reducing the need for manual configuration.
 5. Documentation: Collections can also serve as documentation. You can add descriptions, explanations, and comments to requests within a collection to provide context and instructions for users.


### ENVIRONMENTS

"Environments" are like sets of variables that allow you to adapt your API requests to different contexts or scenarios. They provide a way to configure and customize your requests without having to manually change each one.

 1. Variable Storage: Environments store variables, which are like placeholders for values that can change. These variables can represent things like API keys, server addresses, or user credentials.
 2. Adaptability: You can switch between different environments to quickly adapt your requests. For example, you might have one environment for testing and another for production.
 3. Consistency: Environments help ensure consistency in your requests. Instead of manually editing requests for each environment, you change variables once in the environment, and it affects all requests using those variables.
 4. Security: They are also useful for securely managing sensitive information like API keys. You can store keys in environments, so you don't have to expose them in your requests.

### HTTP REQUESTS

HTTP requests are fundamental to working with Postman. In the Postman environment, you use HTTP requests to interact with APIs and web services.

 1. Types of HTTP Requests: Postman supports various types of HTTP requests, including:
     * GET: Used to retrieve data from a server.
     * POST: Used to send data to a server to create a new resource.
     * PUT: Used to update an existing resource on the server.
     * DELETE: Used to remove a resource from the server.
     * PATCH: Used to apply partial modifications to a resource.
     * And more...

 2. Request Configuration: For each HTTP request, you need to configure several components:
     * HTTP Method: Select the appropriate method for your request (e.g., GET, POST, PUT).
     * URL: Specify the URL of the API endpoint you want to interact with.
     * Headers: Include any necessary headers, such as authentication tokens or content type.
     * Query Parameters: Add query parameters to the URL, if needed.
     * Request Body: Provide data in the request body, especially for POST and PUT requests.

 3. Sending Requests: After configuring the request, you can send it by clicking the "Send" button. Postman will initiate the request and wait for the server's response.
 4. Response Handling: Postman displays the response from the server in a clear and structured format.
     * Response Status: Shows the HTTP status code (e.g., 200 OK, 404 Not Found).
     * Headers: Lists the response headers sent by the server.
     * Response Body: Presents the data returned by the API in various formats (e.g., JSON, XML).

 5. Response Visualization: Postman offers different response visualization options, including "Pretty" for nicely formatted JSON/XML, "Raw" for the raw response, and "Preview" for an interactive view.
 6. Request History: Postman keeps a record of all your previous requests in the "History" tab, allowing you to revisit and reuse requests.
 7. Authentication: Postman provides various authentication methods to access secured APIs, such as Basic Authentication, API keys, OAuth, and more.
 8. Variables: You can use variables in your requests and environments to make them dynamic and adaptable.
 9. Testing and Automation:- Postman enables you to write and run tests to automate the validation of API responses.
