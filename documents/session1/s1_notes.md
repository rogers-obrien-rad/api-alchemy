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

## Subsection 3: [REST and SOAP](https://github.com/rogers-obrien-rad/api-alchemy/blob/main/documents/session1/s1_agenda.md#api-basics-rest-and-soap-10-minutes)


## Subsection 4: [RESTful API Concepts and HTTP Methods](https://github.com/rogers-obrien-rad/api-alchemy/blob/main/documents/session1/s1_agenda.md#restful-api-concepts-and-http-methods-15-minutes)


## Break (10 minutes)

## Subsection 5: [Hands-On: Making API Requests](https://github.com/rogers-obrien-rad/api-alchemy/blob/main/documents/session1/s1_agenda.md#hands-on-making-api-requests-45-minutes)
