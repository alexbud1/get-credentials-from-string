# Get credentials from string

set as argument in get_credentials() your substring with credentials to your database.


function returns an object with fields: engine, name, user, password, host, port

# Usage for Django

Put fetch_db_credentials.py in a directory,where settings.py are placed.

In settings.py import class with following line of code:

    from .fetch_db_credentials import get_credentials
    
Then for using in hosted web-site use the followig code for your databse credentials (engine depends on your database):

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': get_credentials(os.environ['DATABASE_URL']).name,
            'USER': get_credentials(os.environ['DATABASE_URL']).user,
            'PASSWORD': get_credentials(os.environ['DATABASE_URL']).password,
            'HOST': get_credentials(os.environ['DATABASE_URL']).host,
            'PORT':'5432'
        }
    }
