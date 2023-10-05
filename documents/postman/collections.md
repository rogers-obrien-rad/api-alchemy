# CREATING COLLECTIONS
You can create collections in one of two ways:

 1. Directly from the sidebar or
 2. When you save an HTTP request for the first time

## FROM SIDEBAR

 1. Make sure you have the "Collections" tab selected on the sidebar
 2. Just to the right shout be a "+" button. Click this and select "Blank collection"

![image1](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/0a4f5575-a83c-4602-8841-92f2eefd44ac)

 3. You should see a new window pop up in the editor and the name of the collection should be highlighted - name it whatever you like!

![image2](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/fc8def23-e991-4c8e-b5a1-25c8b6043319)

You have successfully created a new collection!


## FROM REQUEST SAVE

Sometimes you might find yourself creating requests before collections. If you want to save any request, you have to save it to a collection. You can create a new collection when you try to save a request:

 1. With a new request open in the editor, select "Save" on the upper right-hand side:

![image3](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/df5cd2b4-3669-4893-9cd1-c7e594ecb4e6)


 2. A dialog window will open and there will be an option at the bottom left to create a "New Collection":

![image4](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/efb5cbf7-9b6a-4c29-a67c-74e8ef8fba96)

 3. You will see a new line added to your list of collections with your cursor in the name box. Name your collection and then hit "Create".

![image5](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/c0b5e9e0-3fdb-40f3-a232-02026b217427)

You have now created a new collection and can save your request there!


# CREATING VARIABLES

Collections are powerful because you can define variables that are specific to the requests within those collections. This is helpful for a few reasons:

 1. Reduce Manual Entry: You don't have to continually type the same value in all the requests
 2. Update Variable Once: Change variable in one location which "waterfalls" to all requests that reference that variable
 3. Security: You can store a token/password within a variable and others can see the variable name but cannot access the value.

Postman has very detailed [variable documentation](https://learning.postman.com/docs/sending-requests/variables).

## FROM COLLECTION

 1. Make sure you have the "Collections" tab selected on the sidebar
 2. Select the collection you want to add a variable to or hover over the name and click the three dots icon and select "Edit"
 3. Your Collection should show up in the editor. In this example, we are showing the "Countries" collection:

![image6](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/9046d796-3149-40b4-852a-0e9e0282da3c)

 4. Select "Variables" from the list of items at the top and you should see:

![image7](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/99dbb28e-0991-4f58-a250-cae83617103c)

 5. From here, you can add a new variable and give it an "Initial" and "Current" value. These names are not very descriptive and are a bit of a misnomer (in our opinion). You can think of them as:
     * Initial: The variable's public value. This value is what others will see when they look at a variable, but it is not used when the variable is referenced in a request.
     * Current: The variables private value. Only people with editor access to the workspace you are in can see this value. This value is what is actually used when the variables is referenced in a request.

> For sensitive information, make sure the "Initial Value" does not match the "Current value". For instance, if you are storing an API token make the initial value something like "Token" and the current value can be the actual string of letters and numbers i.e. "1234abcd".

 6. As soon as you finish typing the variable name, the variable will be created even if data is not in the initial or current values.


## FROM REQUEST SPECIFICATION

Sometimes you don't know what variable you need to define until you start typing the HTTP request endpoint. Postman allows you to create a variable from the request specification.

 1. Highlight the value in your request endpoint that you would like to define as a variable. You should see a small dialog that says "Set as variable" - click this text.

![image8](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/3d0cc04c-4fc1-4b98-863c-7a88c50305d1)


 2. You will see a new dialog window open. If you have a variable already defined that you want to use, select that one. Otherwise, click "Set as new variable":

![image9](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/344a6032-b6af-4c0d-942d-7c6a9640fd80)

 3. You will see a new dialog that will ask you to specify:
     * Name: name of the variable
     * Value: value to assign the variable. The text you highlighted should be defined already.
     * Scope: You can select which requests will have access to this variable. Typically, you will specify by the collection, but you could also choose an environment or "Global" which means all requests would have access to this variable.

![image10](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/43a95039-d6ff-41a9-814d-1184bd5adde6)

> To select a collection as the scope of the variable, you will need to ensure that the request is already saved to that collection otherwise Postman will not let you define the scope to the collection.

 4. Once you have successfully defined the variable, you should see the variable name in double curly braces `{{ }}` in your request:

![image11](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/2532e56c-8c34-4e51-9a1a-074286c4ce9c)


 5. You should also see the variable defined in your collection if you view the collection's variables:

![image12](https://github.com/rogers-obrien-rad/api-alchemy/assets/33231914/f5987840-b3df-4b21-849b-da6cf1083ae7)

---
