import os
_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

ADMINS = frozenset(['youremail@yourdomain.com'])
SECRET_KEY = 'SecretKeyForSessionSigning'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 8

CSRF_ENABLED = True
CSRF_SESSION_KEY = "somethingimpossibletoguess"

# use this in python shell to generate a unique key
# import random
# SECRET_KEY = ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])

RECAPTCHA_USE_SSL = False
RECAPTCHA_PUBLIC_KEY = 'replace with your key'
RECAPTCHA_PRIVATE_KEY = 'replace with your key'
RECAPTCHA_OPTIONS = {'theme': 'white'}

# set to True if you plan to expose DBApy to internet
SECURE_ACCESS = False
