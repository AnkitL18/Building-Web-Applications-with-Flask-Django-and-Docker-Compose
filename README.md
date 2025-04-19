 Flask + Django + Docker Compose Web App
This project demonstrates how to build simple Flask and Django web applications and containerize them using Docker Compose. It also includes a Jenkinsfile for CI/CD automation.

 Features
🔹 Flask App
/ — Displays "Hello, World!"
/greet — Accepts name and age via form, responds with a greeting
Includes basic error handling for invalid inputs
🔹 Django App
Homepage shows a list of items (e.g., books, products, tasks)
Admin panel to add/edit/delete items
Homepage includes a form to add new items
Backed by a SQLite database
🔹 Docker Compose
Separate containers for Flask and Django apps
Flask runs on port 5000, Django on port 8000
Project Structure
final_assignment/ ├── docker-compose.yml
├── flask_app/
│ ├── app.py
│ ├── Dockerfile
│ └── requirements.txt
└── django_app/
├── Dockerfile
├── manage.py
├── requirements.txt
└── django_app/
└── items/

 Getting Started
🛠 Prerequisites
Python 3.9+
Docker
Docker Compose
(Optional) Jenkins
 Local Setup
Step 1: Clone the Repo
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
Step 2: Run with Docker Compose
docker-compose up --build
Step 3: Open in Browser
Flask App: http://localhost:5000

Django App: http://localhost:8000

 Create Django Superuser (Optional for Admin Panel)
docker ps                   # Get Django container name
docker exec -it your_django_container python manage.py createsuperuser
Then visit: http://localhost:8000/admin

 Flask Application Details
flask_app/app.py / route: Returns “Hello, World!”

/greet route: Accepts name & age via form; returns greeting

Handles form validation errors

 Django Application Details
Homepage (Example View) Lists all items in the database

Contains a form to add new item

Model stored in items/models.py

Admin Panel Login at /admin using superuser credentials

Manage all models directly

 Deployment
Push to GitHub: https://github.com/your-username/your-repo-name

Push Docker images to Docker Hub:
