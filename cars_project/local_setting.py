# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0&5isf-os_^y(_j!(0o(kf8h$junfly!-^+g*fw--!ki42)26*'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Cars_database',
        'Host': 'localhost',
        'USER': 'root',
        'PASSWORD': 'hatemenow',
    }
}