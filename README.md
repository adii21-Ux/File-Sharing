# Django File Sharing App

## Introduction
Welcome to the Django File Sharing App! This project is a simple Django web application that allows users to register, upload files, share them with others, and explore user profiles. It's designed to provide a basic file-sharing experience with user authentication and profile management.

## Features
- User Registration and Authentication: Users can create accounts and log in securely.
- File Upload and Sharing: Users can upload files and share them with other registered users.
- Profile Management: Users can view and edit their profiles, including personal information.

## Getting Started
Follow these steps to set up and run the Django File Sharing App locally on your machine.

### Prerequisites
Before you begin, ensure you have the following software installed:

- Python (version 3.x)
- Django
  
#### Installation
1. Clone the Repository:
git clone [https://github.com/your-username/django-file-sharing-app.git](https://github.com/adii21-Ux/File-Sharing.git)

2. Navigate to the Project Directory:
cd django-file-sharing-app

3. Install Dependencies:
pip install -r requirements.txt

4. Perform Database Migrations:
python manage.py migrate

5. Run the Development Server:
python manage.py runserver
The app will be accessible at http://127.0.0.1:8000/ in your web browser.

6. Create a Superuser (Optional):
If you want to access the Django admin panel, create a superuser:
python manage.py createsuperuser

7. Explore the App:
Open your web browser and go to http://127.0.0.1:8000/ to explore the Django File Sharing App. You can register, log in, upload files, and use various features.
