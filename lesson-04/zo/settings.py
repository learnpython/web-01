import os


DIRNAME = os.path.abspath(os.path.dirname(__file__))
rel = lambda *parts: os.path.abspath(os.path.join(DIRNAME, *parts))

# Debug settings
DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Admin settings
ADMINS = (
    ('Igor Davydenko', 'playpauseandstop@gmail.com'),
)
MANAGERS = ADMINS

# Authentication settings
AUTH_PROFILE_MODULE = 'users.UserProfile'

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': rel('..', 'zo.db'),
    }
}

# Date and time settings
TIME_ZONE = 'Europe/Kiev'

# List of installed applications
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.flatpages',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    'annoying',
    'django_extensions',

    'zo',
    'users',
)

# I18n and l10n settings
LANGUAGE_CODE = 'ru'
USE_I18N = True
USE_L10N = True
USE_TZ = False

# Logging settings
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Media and static files settings
MEDIA_ROOT = rel('..', 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = rel('..', 'static')
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Middleware classes
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

# Template settings
TEMPLATE_DIRS = (
    rel('templates'),
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# Other Django settings
ROOT_URLCONF = 'zo.urls'
SECRET_KEY = 'please, set proper value in settings_local.py'
SITE_ID = 1
WSGI_APPLICATION = 'zo.wsgi.application'


try:
    import settings_local
except ImportError:
    pass
else:
    for attr in dir(settings_local):
        if attr.startswith('_'):
            continue
        locals()[attr] = getattr(settings_local, attr)
