DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'base_de_dados',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'usuario',
        'PASSWORD': 'senha',

    }
}

SECURE_PROXY_SSL_HEADER = None
SECURE_SSL_REDIRECT = None
SESSION_COOKIE_SECURE = None
CSRF_COOKIE_SECURE = None