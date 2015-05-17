import os

from .settings import *

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'smartboardweb',                      # Or path to database file if using sqlite3.
            'USER': 'admin',
            'PASSWORD': 'secretpassword',
            'HOST': 'localhost',                      # Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP.
            'PORT': '',                      # Set to empty string for default.
        }
    }

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')