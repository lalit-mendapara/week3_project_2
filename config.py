import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER") # Email id
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD") # Email app password

CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL") # redis server url
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND") # redis server Url

SECRET_KEY = os.getenv("SECRET_KEY") # django secret key