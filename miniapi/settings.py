"""
Django settings for miniapi project.
"""

from pathlib import Path
import os

# --- BASE ---
BASE_DIR = Path(__file__).resolve().parent.parent

# --- SECURITY ---
SECRET_KEY = 'django-insecure-xzcl_e%f8cweo8*m8_bur4#cs&4$_q7rywny+cr=43+xh^_8fd'
DEBUG = True  # ⚠️ Cámbialo a False cuando termines de probar
ALLOWED_HOSTS = ['*']  # En producción: ['tu_usuario.pythonanywhere.com']

# --- APPS ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'api',
]

# --- MIDDLEWARE ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# --- URL & WSGI ---
ROOT_URLCONF = 'miniapi.urls'
WSGI_APPLICATION = 'miniapi.wsgi.application'

# --- DATABASE ---
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# --- TEMPLATES ---
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'web')],
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

# --- PASSWORD VALIDATION ---
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --- INTERNATIONALIZATION ---
LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'America/Mexico_City'
USE_I18N = True
USE_TZ = True

# --- STATIC FILES ---
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'web')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # ✅ Necesario para PythonAnywhere

# --- DEFAULT PRIMARY KEY FIELD TYPE ---
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
