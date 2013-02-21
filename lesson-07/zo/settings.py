import os


DIRNAME = os.path.abspath(os.path.dirname(__file__))
rel = lambda *parts: os.path.abspath(os.path.join(DIRNAME, *parts))
_ = lambda s: s

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
    'grappelli.dashboard',
    'grappelli',
    'filebrowser',

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
    'debug_toolbar',
    'django_extensions',
    'haystack',
    'south',

    'zo',
    'bookmarks',
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

# Filebrowser, media and static files settings
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
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
)
TEMPLATE_DIRS = (
    rel('templates'),
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# Other Django settings
INTERNAL_IPS = ('127.0.0.1', )
ROOT_URLCONF = 'zo.urls'
SECRET_KEY = 'please, set proper value in settings_local.py'
SITE_ID = 1
WSGI_APPLICATION = 'zo.wsgi.application'

# Grappelli settings
GRAPPELLI_ADMIN_TITLE = _('Zapis Online')
GRAPPELLI_INDEX_DASHBOARD = 'zo.admin.AdminDashboard'

# Haystack settings
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': rel('..', 'whoosh_index'),
        'INCLUDE_SPELLINGS': True,
    },
}


# Load local settings
try:
    import settings_local
except ImportError:
    pass
else:
    for attr in dir(settings_local):
        if attr.startswith('_'):
            continue
        locals()[attr] = getattr(settings_local, attr)


# Debug toolbar settings
if DEBUG:
    MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )

    DEBUG_TOOLBAR_PANELS = (
        'debug_toolbar.panels.version.VersionDebugPanel',
        'debug_toolbar.panels.timer.TimerDebugPanel',
        'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
        'debug_toolbar.panels.headers.HeaderDebugPanel',
        'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
        'debug_toolbar.panels.template.TemplateDebugPanel',
        'debug_toolbar.panels.sql.SQLDebugPanel',
        'debug_toolbar.panels.signals.SignalDebugPanel',
        'debug_toolbar.panels.logger.LoggingPanel',
    )
    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
        'SHOW_TEMPLATE_CONTEXT': True,
    }
