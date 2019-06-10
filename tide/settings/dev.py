from tide.settings.base import *

#Override base settings here
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
SECRET_KEY = 'mj-+%*k0(61okn)^4@@(@%f46d!e52=8o0lnunmo9@xq!qaia@'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



try:
	from tide.settings.local import *
except:
	pass