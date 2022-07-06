# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'database_name',
        'USER': 'database_user',
        'PASSWORD': 'database_password',
        'HOST': 'database_host',
        'PORT': 5432,
        'CHARSET': 'UTF-8',
        'OPTIONS': {
            'options': '-c search_path=staging'
        },
    }
}
