import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f#j8w41o6xx_2!g%y#lv^-us9jht9wb89^5^$=rfsdpi4(%p6-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS += [
    'crispy_forms',
    'django_summernote_ajax',
    'sandbox_app',
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

ROOT_URLCONF = 'sandbox.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'sandbox.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/assets/'
STATIC_ROOT = os.path.join(BASE_DIR, 'sandbox/assets/')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'sandbox_app/static/'),
    os.path.join(BASE_DIR, 'django_summernote_ajax/static/'),
]

# Media files (Uploaded files)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'sandbox/media/')

# Crispy Form
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Django Summernote Ajax Settings
# The content-type header uploaded with the file (default: ['image', 'video'])
DSA_CONTENT_TYPES = ['image', 'video']
# The allowed file extensions (default: ['jpg', 'jpeg', 'gif', 'png'])
DSA_FILE_EXTENSIONS = ['jpg', 'jpeg', 'gif', 'png']
# The size, in bytes, of the uploaded file (default: 2MB)
DSA_MAX_UPLOAD_SIZE = 2097152

# The maximum number of uploaded files
POST_MAX_FILE_COUNT = 10

# URLs for file upload and download
POST_FILE_UPLOAD_URL = '/upload-file'
POST_FILE_DELETE_URL = '/delete-file'

# Celery / RabbitMQ
CELERY_BROKER_URL = 'amqp://localhost//'
