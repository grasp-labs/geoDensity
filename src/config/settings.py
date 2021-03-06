"""
Django settings for microservice project.
Generated by 'django-admin startproject' using Django 3.1.1.
For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
import configparser
from datetime import timedelta


# Setting up configparser
CONFIG = configparser.ConfigParser()

# identify project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CONFIG.read(os.path.join(BASE_DIR, 'config/config.ini'))

# Collecting secrets
CONFIG.set('DATABASE', 'Host', os.environ.get('DB_HOST'))
CONFIG.set('DATABASE', 'Database', os.environ.get('DB_NAME'))
CONFIG.set('DATABASE', 'User', os.environ.get('DB_USER'))
CONFIG.set('DATABASE', 'Password', os.environ.get('DB_PASSWORD'))

# SECURITY WARNING: keep the secret key used in production secret!
DEBUG = CONFIG['GENERAL']['Debug']
ADMIN_INITIAL_PASSWORD = CONFIG['GENERAL']['InitialAdminPass']
SECRET_KEY = CONFIG['GENERAL']['Django_secret']

allowed_hosts = list(CONFIG['GENERAL']['AllowedHosts'].split('|'))
ALLOWED_HOSTS = allowed_hosts

# Default Admins
ADMINS = (
    ('superuser', 'super@user.no'),
)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third party apps
    # custom apps
    'geodensity.apps.GeodensityConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'config/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': CONFIG['LOCAL_DB']['Database'],
        'USER': CONFIG['LOCAL_DB']['User'],
        'PASSWORD': CONFIG['LOCAL_DB']['Password'],
        'HOST': CONFIG['LOCAL_DB']['Host'],
        'PORT': CONFIG['LOCAL_DB']['Port']
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_URL = '/static/'
