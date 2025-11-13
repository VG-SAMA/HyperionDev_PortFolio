# Sticky Notes Django App with TestCase

# Overview

This folder is the same as part one, just with testings done.
This is a simple Sticky Notes web application built with Django.
It demonstrates the Model-View-Template (MVT) architecture, CRUD functionality, and usage of static files for styling. Users can create, read, update, and delete notes with a clean interface.

# How to run tests:

Clone the repository
git clone <repo-url>
cd PracticalTask
run venv/scripts/activate
cd sticky_notes
python manage.py test notes

## Features

Create new sticky notes with a title and content
View a list of all notes
Update existing notes
Delete notes with a confirmation step
Basic CSS, Bootstrap styling for clean UI
Supports global static assets (images, favicon, etc.)

# Installation

Clone the repository
git clone <repo-url>
cd PracticalTask
cd sticky_notes

# Create a virtual environment and activate it

python -m venv venv

- Windows
- venv\Scripts\activate
- macOS/Linux
- source venv/bin/activate

# Install dependencies

- pip install -r requirements.txt

# Create a superuser (optional, for admin access)

- python manage.py createsuperuser

# Run the development server

Please navigate (cd) into PracticalTask -> sticky_notes

- python manage.py runserver

# Access the app

Open your browser and go to:

http://127.0.0.1:8000/

# Project Structure

PracticalTask/
├── notes/ # Django app
│ ├── migrations/
│ ├── static/ # App-specific static files (CSS, images)
│ │ └── notes/
│ └── templates/notes/ # App-specific templates
├── sticky_notes/ # Project settings
│ └── settings.py
├── static/ # Global static files (favicon, shared images)
├── templates/ # Optional global templates
├── requirements.txt # Python dependencies
├── manage.py
└── README.md

# Reference:

# Django Software Foundation (2025). Working with QuerySets and filters.

# https://docs.djangoproject.com/en/5.1/topics/db/queries/#retrieving-specific-objects-with-filters

# Django Software Foundation (2025). The GET and POST methods.

# https://docs.djangoproject.com/en/5.1/topics/forms/#the-get-and-post-methods

# Bootstrap 5 Documentation – Form controls and Buttons.

# https://getbootstrap.com/docs/5.3/forms/overview/
