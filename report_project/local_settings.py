
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-passsylgsdioef=q&nj=&c^!%6(l17jxijdz=aj+w9zg#_g^&a'




# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'report_database',
        'HOST' : 'localhost',
        'USER' : 'root',
        'PASSWORD' : 'password' 
    }
}

