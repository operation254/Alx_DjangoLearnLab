# Django Blog

A Django blog application with authentication, posts CRUD, comments, tagging, and search.

## Features
- User registration, login, logout, profile edit
- Posts: create, read, update, delete (author-only edit/delete)
- Comments: create, update, delete (author-only edit/delete)
- Tags (django-taggit)
- Search by title, content, and tag name

## Setup
```bash
cd django_blog
python -m pip install django django-taggit
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
