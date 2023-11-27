### Branch Messaging Web Application
Welcome to the Branch Messaging Web Application project! This application is designed to address the challenge of handling a high volume of customer inquiries. The primary goal is to build a messaging platform that enables a team of agents to respond to customer questions efficiently. This readme provides instructions on setting up and running the messaging web application.

### Project Overview
## Objective
A messaging web application that allows a team of agents to respond to incoming questions from customers. The application should scale as the customer base grows, and it supports multiple agents logging in simultaneously.

## Features
1. Messaging System:

- Agents can respond to incoming customer questions.
- Streamlined interface for efficient communication.

2. API Endpoint:

- Simulate customer messages through an API endpoint.
- Messages can be sent and received through a web form or Postman collection.

3. Database Integration:

- Store real customer service messages provided in a CSV file in a chosen database.
- Agents can view and respond to individual messages in the application.

### Setup Instructions
Follow these steps to set up and run the messaging web application:

## Prerequisites
- Node.js installed on your machine.
- React for building the frontend.
- Python installed for backend development.
- Flask for building the backend.

### Backend Setup
Open another terminal and navigate to the project's backend directory:
    ```bash

cd branch-messaging-backend
cd server
## Install dependencies and activate the virtual environment:


pipenv install </br>
pipenv shell</br>
## Run the Flask server:


flask run </br>
or

</br>

python app.py </br>  

Ensure the backend server is running at http://localhost:5000.

## API Endpoint and Database
Simulate customer messages using the provided API endpoint or web form.
Store real customer service messages in the database.
View and respond to individual messages through the application.

GET /messages: returns an array of all messages as JSON, ordered by created_at in ascending order. </br></br>
POST /messages: creates a new message with a body and username from params, and returns the newly created post as JSON. </br></br>
PATCH /messages/<int:id>: updates the body of the message using params, and returns the updated message as JSON. </br></br>
DELETE /messages/<int:id>: deletes the message from the database. 

## Additional Notes
The application is designed for ease of use and scalability.

## Contact
For any inquiries or support, please contact me , at judieysiggy@gmail.com

## License
This project is licensed under the MIT License.