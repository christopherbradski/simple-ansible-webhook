import ansible_runner
import os

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
    if os.path.exists(f'/src/ansible/keys/amiga'):
        with open(f'/src/ansible/keys/amiga', 'r') as f:
            SSH_KEY = f.read()
    runner = ansible_runner.run(private_data_dir='/src/ansible/roles/docker_dns/tasks', 
                                playbook='main.yml', 
                                inventory=f'{hostname}', 
                                extravars={'ansible_ssh_private_key_file': '/src/ansible/keys/amiga',
                                           'ansible_port': 22222},
                                )
    print("{}: {}".format(runner.status, runner.rc))
    print("Final status:")
    status = f"{runner.stats}"
    return status
