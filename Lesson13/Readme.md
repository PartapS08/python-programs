### Index ###

    - Django Framework

#### Description ####

Django is a high-level Python web framework. A Framework is predefined structure of web application, which defines how to build the application. Django follows the Model-View-Controller (MVC) structure or also refered as Model-View-Template (MVT).
- <b>MVC Pattern</b>
    - <b>Model:</b> Defines the data structure (database schema).
    - <b>View:</b> Handles the logic and control of what the user sees.
    - <b>Template:</b> Manages the presentation and rendering of HTML/CSS.
- <b>URL Routing:</b> Django’s URL dispatcher helps in mapping URLs to views.
- <b>Admin Interface:</b> Django provides a built-in admin interface for managing application data

#### Getting Started ####

Prerequisite:</br>
Python must be installed on your system/server.

Installation:
```
pip install django
```
Creating Project 'myproject' in Django
```
django-admin startproject myproject
cd myproject
```
Creating App inside the Project
```
python manage.py startapp myapp
```
Running the Project
```
python manage.py runserver
```
