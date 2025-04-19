Building Web Applications with Flask, Django, and Docker Compose
Project Overview
This project involves creating two web applications — one using Flask and the other using Django — and containerizing them using Docker. The two applications are:

Flask Application:

Displays a "Hello, World!" message on the homepage.

Includes a form to accept the user's name and age and returns a personalized greeting message.

Implements basic error handling for invalid inputs.

Django Application:

Displays a list of items (e.g., books, tasks, products) stored in a database.

Provides an admin panel for managing the items.

Includes a form to add new items to the list.

Both applications are containerized using Docker Compose and accessible on separate ports.

Project Structure
Copy
Edit
├── flask/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── django/
│   ├── manage.py
│   ├── Dockerfile
│   └── requirements.txt
├── docker-compose.yml
├── README.md
└── Jenkinsfile
Requirements
Docker: To containerize the applications.

Docker Compose: To manage the multi-container setup.

Python (Flask and Django dependencies):

Flask (for the Flask application)

Django (for the Django application)

How to Run the Project Locally
1. Clone the Repository
Clone the repository to your local machine:

bash
Copy
Edit
git clone <your-github-repo-url>
cd <your-repo-directory>
2. Build and Run the Applications Using Docker Compose
Make sure you have Docker and Docker Compose installed on your system.

Run the following command to build and start both the Flask and Django containers:

bash
Copy
Edit
docker-compose up --build
This will:

Build the Flask and Django images using their respective Dockerfile.

Start the containers and make the applications accessible on separate ports.

3. Access the Applications
The Flask application will be accessible at http://localhost:5000.

The Django application will be accessible at http://localhost:8000.

4. Stopping the Containers
To stop the containers, use the following command:

bash
Copy
Edit
docker-compose down
Project Details
Flask Application
Homepage: Displays a "Hello, World!" message.

Form: Accepts user input (name and age), then displays a personalized greeting.

Error Handling: Provides a message if the user inputs invalid data (e.g., non-numeric age).

Django Application
Homepage: Displays a list of items from the database (e.g., books, tasks, products).

Admin Panel: Allows admins to add, modify, or delete items from the list.

Add Item Form: Provides a form on the homepage to add new items to the list.

Docker Setup
Dockerfile for Flask
The Dockerfile for the Flask application includes steps to set up a Python environment, install the dependencies, and run the app.

Dockerfile for Django
The Dockerfile for the Django application sets up a Python environment, installs the necessary dependencies, and starts the Django server.

docker-compose.yml
This file defines the services (Flask and Django), their build contexts, and the ports each application should be exposed on.


