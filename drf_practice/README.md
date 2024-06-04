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
