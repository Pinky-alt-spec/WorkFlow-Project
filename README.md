# Customer Financial Data Management System

This project is a web-based workflow system developed in Python using the Django framework. It allows users to enter customer information, upload an Excel file containing financial income and expenses for the last 12 months, and visualize the data through temporal graphs.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [Usage](#usage)

## Features
- Capture customer information (First Name, Last Name, Date of Birth).
- Upload an Excel file containing financial data.
- Visualize income and expenses over the last 12 months in a graph.

## Prerequisites
- Python 3.x
- Django 3.x or later
- pandas
- matplotlib
- tablib
- django-import-export
- SQLite (default database)

## Installation

### 1. Clone the repository
#### Clone the project to your local code editor (e.g. vscode)
```bash
git clone https://github.com/Pinky-alt-spec/WorkFlow-Project.git
cd workflow_project
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```
### 3. Install dependencies
```bash
pip freeze > requirements.txt
```

## Running the Project

### 1. Apply database migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 2. Create a superuser
```bash
python manage.py createsuperuser
```
### 3. Run the development server
```bash
python manage.py runserver
```
### 4. Access the application
```bash
Open your web browser and go to http://127.0.0.1:8000/
```

## Usage

### 1. Upload Customer Information and Financial Data
Go to http://127.0.0.1:8000/customer/upload/
Fill in the customer information form.
Upload an Excel file with the customer's financial data.
Upload the form.

### 2. View Financial Data Graph
After submitting the form, you will be redirected to a page showing a graph of the customer's income and expenses over the last 12 months.

## Project Structure
```bash
customer_app/
    ├── migrations/
    ├── templates/
        ├── customer_graph.html
        ├── upload_customer.html
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    ├── views.py
workflow_project/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── wsgi.py
db.sqlite3
manage.py
README.md
requirements.txt
```
