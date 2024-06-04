Installation command for DRF
step 1: Make virtual Environment
    python -m venv venv

step 2: Install Django 
    pip install django

step 3: Make  App 
    python manage.py startapp appname

step4: Install Django Rest Framework
    pip install djangorestframework

step 5: register your app and django rest framework in setting py. file in projetc folder
    INSTALLED_APPS = [
        ...
        'rest_framework',
        'appname',
    ]
step 6: Chango database into PostgreSQL
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "DRF",
            "USER": "postgres",
            "PASSWORD":"swan",
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }
step 6 : migration commands
    python manage.py makemigrations
    python manage.py migrate


To create token commandline Token and if token is generated then token will existing token  
    - python manage.py drf_create_token (username)


access 1 : 
    username : admin
    password : admin

access 2 : 
    username : keval
    password : Vasani@1

access 3:
    username : admin2
    password : User@123

access 4:
    username : admin3
    password : User@123

access 5:
    username : admin4
    password : User@123

To install client token ask 
    - pip install httpie


token generate 




install JWTtoken -> JSON Web Token
    - pip install djangorestframework-simplejwt

