from app.config.settings import CELERY_CONFIG
from celery import Celery

# Celery configuration
celery = Celery(
    'worker',
    broker=CELERY_CONFIG['broker_url'],
    backend=CELERY_CONFIG['result_backend']
)

# Create a task function
@celery.task()
def fix_docker_dns(hostname: str):
    status = "success"
    return status