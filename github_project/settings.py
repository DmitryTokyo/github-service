from pathlib import Path, PurePath
from configurations import Configuration, values


class Dev(Configuration):
    ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
    APPS_DIR = ROOT_DIR / 'pulls'

    DEBUG = values.BooleanValue(True)

    SECRET_KEY = values.SecretValue()

    GITHUB_TOKEN = values.Value(environ_name='TOKEN')

    ALLOWED_HOSTS = ['127.0.0.1']

    # Application definition

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        'pulls',
        'waffle',
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',

        'waffle.middleware.WaffleMiddleware',
    ]

    ROOT_URLCONF = 'github_project.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [PurePath(ROOT_DIR).joinpath('templates/')],
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

    WSGI_APPLICATION = 'github_project.wsgi.application'

    # Database
    # https://docs.djangoproject.com/en/3.2/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'sqlite.db',
        }
    }

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
            'LOCATION': '/var/tmp/django_cache',
            'TIMEOUT': 3600,
        }
    }

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

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True


    STATIC_URL = '/static/'

    STATICFILES_DIRS = [
        PurePath(ROOT_DIR).joinpath('static')
    ]

    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
