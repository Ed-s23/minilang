from pathlib import Path
import os

# BASE_DIR apunta a la raíz del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# ⚠️ En producción deberías usar una variable de entorno para la clave secreta
SECRET_KEY = 'django-insecure-xzcl_e%f8cweo8*m8_bur4#cs&4$_q7rywny+cr=43+xh^_8fd'

DEBUG = True  # Cambia a False en producción

# ✅ Acepta todos los hosts (útil para PythonAnywhere y pruebas locales)
ALLOWED_HOSTS = ['*']

# -------------------- APPS --------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Apps externas
    'rest_framework',

    # Tu app local
    'api',
]

# -------------------- MIDDLEWARE --------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# -------------------- URLs y WSGI --------------------
ROOT_URLCONF = 'miniapi.urls'
WSGI_APPLICATION = 'miniapi.wsgi.application'

# -------------------- BASE DE DATOS --------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# -------------------- TEMPLATES --------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        # ✅ Aquí Django buscará tus HTML (como web/index.html)
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

# -------------------- LOCALIZACIÓN --------------------
LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'America/Mexico_City'
USE_I18N = True
USE_TZ = True

# -------------------- ARCHIVOS ESTÁTICOS --------------------
# URL base para archivos estáticos (CSS, JS, imágenes)
STATIC_URL = '/static/'

# ✅ Aquí Django buscará tus archivos estáticos durante el desarrollo
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'web'),  # tu carpeta con style.css
]

# ✅ Aquí se recopilan los archivos cuando haces `collectstatic`
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# -------------------- CONFIG FINAL --------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
