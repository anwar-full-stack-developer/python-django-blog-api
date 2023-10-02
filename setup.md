## Setting up Django REST framework

Create a virtual environment to isolate dependencies, however, this is optional. 

 Run the command `python -m venv django_env` from inside your projects folder to create the virtual environment. Then, run `source ./django_env/bin/activate` (Linux/Mac) to turn it on.
 In windows run `.\django_env\bin\activate` (Windows) to turn it on.

## Navigate to an empty folder in your terminal and install Django and Django REST framework in your project with the commands below:

`pip install django`
`pip install django_rest_framework`

## Create a Django project called `blog` with the following command:

`django-admin startproject blog`

## Then, cd into the new blog folder and create a new app for your API:

`django-admin startapp blog_api`

`python manage.py migrate`


## create a superuser

`python manage.py createsuperuser` 

in some case createsuperuser command does not work, try command bellow

`winpty python manage.py createsuperuser`
//It should work by just appending 'winpty' before the command

## Create a Model, After creating the model, migrate it to the database.

`python manage.py makemigrations`
`python manage.py migrate`

## Run Server

`python manage.py runserver`