"""
Django settings for blog project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path
from django.contrib.messages import constants
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'tx82rt7q0@so==u^m9nbleolqou8*p8(4^-&q3s^%h(^xfb&8y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["samysantos10.pythonanywhere.com"]


# Application definition

INSTALLED_APPS = [
    'accounts',
    'post',
    'comentarios',
    'categorias',
    'blog_email',
    'notificaçoes',
    'social_django',
    'post.templatetags.filters',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'axes',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'axes.middleware.AxesMiddleware',
]

ROOT_URLCONF = 'blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
  'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'samysantos10$Blog',
        'HOST': 'samysantos10.mysql.pythonanywhere-services.com',
        'PORT': '3306',
        'USER': 'samysantos10',
        'PASSWORD': 'S@my4667',
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

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = '/home/samysantos10/Projeto_blog_Django/static'

STATICFILES_DIRS = (os.path.join(BASE_DIR, "files"),)

# Para o usuario poder adicionar mídias, fazer as configurações abaixo.
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join (BASE_DIR, 'midias/')

# Messages
# Os alertas vão na classe da tag no template
MESSAGE_TAGS = {
    constants.INFO: 'alert-info',
    constants.SUCCESS: 'alert-success',
    constants.WARNING: 'alert-warning',
    constants.ERROR: 'alert-error',
    constants.DEBUG: 'alert-info',
}

# Configuração Django-Summernote
INSTALLED_APPS += ('django_summernote',)
X_FRAME_OPTIONS = 'SAMEORIGIN'


# Configuração rede social
AUTHENTICATION_BACKENDS = (
    'axes.backends.AxesBackend',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.google.GoogleOAuth2',

    'django.contrib.auth.backends.ModelBackend',
)

# Autenticação pelo facebook
SOCIAL_AUTH_FACEBOOK_KEY = '414184179999238'
SOCIAL_AUTH_FACEBOOK_SECRET = 'd68fed2d64092e2cb32bc5fadf800682'

# Autenticação pelo Github
SOCIAL_AUTH_GITHUB_KEY = 'a4a0697de7ac8fb277e2'
SOCIAL_AUTH_GITHUB_SECRET = '35585559b09ce930e09bfa9cf1327ae469766ff4'

# Autenticação pelo Google
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '955161584054-ocobrnmng47tj4625kk4rtsbojqbukjf.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'EOQ-7TD62FBMBmNfdwqulvgy'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'


##### CONFIGURAÇÕES DO DO AXE #####

# Defini o limite de tentativas do usuario
AXES_FAILURE_LIMIT = 5

# # AXES_ENABLE_ADMIN = True

# Bloqueia com base no nome do usuario
AXES_ONLY_USER_FAILURES = True

# redefini o numero de tentativas após UMA tentativa bem-sucedida
AXES_RESET_ON_SUCCESS = True

# Defini o tempo de bloqueio
AXES_COOLOFF_TIME = timedelta(minutes=30)

# redireciona o usuario para este template quando bloqueado
AXES_LOCKOUT_TEMPLATE = 'accounts/locked.html'


SECURE_PROXY_SSL_HEADER = None
SECURE_SSL_REDIRECT = None
SESSION_COOKIE_SECURE = None
CSRF_COOKIE_SECURE = None

try:
    from .local_settings import *

except:
    pass
