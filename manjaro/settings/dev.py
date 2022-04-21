from .base import *
import os

INSTALLED_APPS = INSTALLED_APPS + [
    'django_browser_reload',
]

MIDDLEWARE = MIDDLEWARE + [
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0s_dy9yon+m^ibos)el*-nez^t7-gh%f#r^ma9&9$$(osaou^i'
RECAPTCHA_PUBLIC_KEY = '6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI'
RECAPTCHA_PRIVATE_KEY = '6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe'

SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CSRF_COOKIE_SECURE = False
SECURE_HSTS_SECONDS = False
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False

try:
    from .local import *
except ImportError:
    pass
