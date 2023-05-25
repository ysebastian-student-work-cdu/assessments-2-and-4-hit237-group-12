## Tio create the virtual environment ##
virtualenv env
env\Scripts\activate

## To install the django ##

pip install Django

## To create the djano project

django-admin startproject assignment

python manage.py startapp myapp

## To start the djano application ##

python manage.py runserver

## Visit the following link ##

http://127.0.0.1:8000/

## For migration ##

python manage.py makemigrations
python manage.py migrate

## To create the superuser account ##

python manage.py createsuperuser
