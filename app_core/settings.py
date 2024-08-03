import os
from datetime import timedelta
from pathlib import Path

from django.utils.translation import gettext_lazy as _
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

DEBUG = bool(os.getenv('DJANGO_DEBUG'))

if ',' in os.getenv('DJANGO_ALLOWED_HOSTS'):
    ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS').split(',')
else:
    ALLOWED_HOSTS = [os.getenv('DJANGO_ALLOWED_HOSTS')]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
]

THIRD_PARTY_APPS = [
    'auditlog',
    'corsheaders',
    'drf_yasg',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'django_cleanup.apps.CleanupConfig',
    'django_filters',
    'adminsortable2',
    'import_export',
    'whitenoise.runserver_nostatic',
    'django_ckeditor_5',
    'parler',
    'rosetta'
]

CUSTOM_APPS = [
    'apps.common.utils',
    'apps.common.serverhttp',

    'apps.project.common.users',

    'apps.project.page.index',
]

SPIRIT_APPS = [
    'apps.project.spirit.spirit_core',
    'apps.project.spirit.ramptwo',
    'apps.project.spirit.rampone',
    'apps.project.spirit.pbe',
    'apps.project.spirit.door',
    'apps.project.spirit.baggage'
]

ALL_CUSTOM_APPS = CUSTOM_APPS + SPIRIT_APPS

LOCALE_PATHS = [
    app_path / 'locale' for app_path in [BASE_DIR / app.replace('.', '/') for app in ALL_CUSTOM_APPS]
]

LOCALE_PATHS.append(str(BASE_DIR / 'app_core' / 'locale'))

INSTALLED_APPS = THIRD_PARTY_APPS + DJANGO_APPS + ALL_CUSTOM_APPS

UTILS_PATH = 'apps.common.utils'

ADMIN_URL = os.getenv('DJANGO_ADMIN_URL')

if os.getenv('DJANGO_SECURE_SSL_REDIRECT') == 'True':
    SECURE_SSL_REDIRECT = True
else:
    SECURE_SSL_REDIRECT = False

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'auditlog.middleware.AuditlogMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'apps.common.utils.middleware.APILogMiddleware',
]

MIDDLEWARE_NOT_INCLUDE = [os.getenv('MIDDLEWARE_NOT_INCLUDE')]

ROOT_URLCONF = 'app_core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'apps'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                f'{UTILS_PATH}.context_processors.custom_processors'
            ],
        },
    },
]

WSGI_APPLICATION = 'app_core.wsgi.application'

DATABASES = {
    'default': {
        'CONN_MAX_AGE': int(os.getenv('DB_CONN_MAX_AGE')),
        'ENGINE': os.getenv('DB_ENGINE'),
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': int(os.getenv('DB_PORT')),
        'CHARSET': os.getenv('DB_CHARSET'),
        'ATOMIC_REQUESTS': True
    }
}

SESSION_EXPIRE_AT_BROWSER_CLOSE = False

SESSION_COOKIE_AGE = 7200

AUTH_USER_MODEL = 'users.UserModel'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    f'{UTILS_PATH}.backend.EmailUsernameEmployeeIDModelBackend',
]

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]

LANGUAGE_CODE = 'en'

USE_TZ = True

TIME_ZONE = 'America/Bogota'

LANGUAGES = [
    ('es', _('Spanish')),
    ('en', _('English'))
]

PARLER_LANGUAGES = {
    None: (
        {'code': 'es', },
        {'code': 'en', },
    ),
    'default': {
        'fallbacks': ['en'],
        'hide_untranslated': False,
    }
}

ROSETTA_SHOW_AT_ADMIN_PANEL = True

USE_I18N = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


STATIC_ROOT = str(BASE_DIR / 'public' / 'staticfiles')

STATIC_URL = 'public/static/'

STATICFILES_DIRS = [str(BASE_DIR / 'public' / 'static')]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

MEDIA_ROOT = str(BASE_DIR / 'public' / 'media')

MEDIA_URL = "public/media/"

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

if bool(os.getenv('DJANGO_EMAIL_USE_SSL')):
    EMAIL_USE_SSL = True
    EMAIL_USE_TLS = False
else:
    EMAIL_USE_SSL = False
    EMAIL_USE_TLS = True

EMAIL_BACKEND = os.getenv('DJANGO_EMAIL_BACKEND')
EMAIL_HOST_USER = os.getenv('DJANGO_EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('DJANGO_EMAIL_HOST_PASSWORD')
EMAIL_HOST = os.getenv('DJANGO_EMAIL_HOST', 'mail.fundacionleirion.com')
EMAIL_PORT = int(os.getenv('DJANGO_EMAIL_PORT'))
DEFAULT_FROM_EMAIL = os.getenv('DJANGO_EMAIL_DEFAULT_FROM_EMAIL')

customColorPalette = [
    {
        'color': 'hsl(4, 90%, 58%)',
        'label': 'Red'
    },
    {
        'color': 'hsl(340, 82%, 52%)',
        'label': 'Pink'
    },
    {
        'color': 'hsl(291, 64%, 42%)',
        'label': 'Purple'
    },
    {
        'color': 'hsl(262, 52%, 47%)',
        'label': 'Deep Purple'
    },
    {
        'color': 'hsl(231, 48%, 48%)',
        'label': 'Indigo'
    },
    {
        'color': 'hsl(207, 90%, 54%)',
        'label': 'Blue'
    },
]

CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': [
            'heading', '|',
            'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor', 'removeFormat', '|',
            'bold', 'italic', 'underline', 'strikethrough', 'code', 'link', 'subscript', 'superscript', '|',
            'bulletedList', 'numberedList', 'todoList', '|',
            'insertImage', 'mediaEmbed', '|',
            'outdent', 'indent', '|',
            'blockQuote', 'insertTable', '|',
            'sourceEditing',
        ],
    },
    'list': {
        'properties': {
            'styles': 'true',
            'startIndex': 'true',
            'reversed': 'true',
        }
    }
}

CKEDITOR_5_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

SWAGGER_SETTINGS = {
    'USE_SESSION_AUTH': True,
    'SECURITY_DEFINITIONS': {
        'Basic': {
            'type': 'basic'
        },
    }
}

YASG_DEFAULT_EMAIL = os.getenv('YASG_DEFAULT_EMAIL')
YASG_TERMS_OF_SERVICE = os.getenv('YASG_TERMS_OF_SERVICE')

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}

SPIRIT_PERMISSION_GROUP_NAME = os.getenv('SPIRIT_PERMISSION_GROUP_NAME')
SPIRIT_SUPERVISOR_PERMISSION_GROUP_NAME = os.getenv('SPIRIT_SUPERVISOR_PERMISSION_GROUP_NAME')