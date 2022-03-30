from .base import *
import django_heroku

DEBUG = False

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_PORT = 2525
EMAIL_USE_TLS = True

# CLOUDINARY SETUP FOR FILE STORAGE
DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.RawMediaCloudinaryStorage"
CLOUDINARY_STORAGE = {
    "CLOUD_NAME": env(("CLOUDINARY_CLOUD_NAME")),
    "API_KEY": env(("CLOUDINARY_API_KEY")),
    "API_SECRET": env(("CLOUDINARY_API_SECRET")),
}

# heroku configuration
django_heroku.settings(locals())
