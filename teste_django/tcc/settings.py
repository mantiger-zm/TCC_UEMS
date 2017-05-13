# -*- coding: utf-8 -*-
# Construa caminhos dentro do projeto como este: os.path.join(BASE_DIR, ...)
# import os
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# Unipath aqui
from unipath import Path
BASE_DIR = Path(__file__).parent




# AVISO DE SEGURANÇA: mantenha a chave secreta usada em segredo de produçao
SECRET_KEY = 'z_e56zqn)721@cu*gsgtf&elh(sobueh@jul2o*4(cm$lj-%%^'

# AVISO DE SEGURANÇA: não execute com depuração ativada na produção!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Definição da aplicação

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'grafico',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'tcc.urls'

WSGI_APPLICATION = 'tcc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME': 'sqlite3-db',
        'ATOMIC_REQUESTS': True  # Unipath aqui
    }
}

# Internacializacao


LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Arquivos estáticos (CSS, JavaScript, Images)


STATIC_URL = '/static/'
