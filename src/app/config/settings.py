import os
from distutils.util import strtobool

SECRET_KEY = os.getenv("SECRET_KEY", None)

SERVER_NAME = os.getenv(
    "SERVER_NAME", "localhost:{0}".format(os.getenv("DOCKER_WEB_PORT", "8192"))
)

# Redis
REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")

# Celery
CELERY_CONFIG = {
    "broker_url": REDIS_URL,
    "result_backend": REDIS_URL,
}