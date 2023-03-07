# Create a flask app

from flask import Flask
from app.celery_tasks import fix_docker_dns

app = Flask(__name__)

# Create a route to call the task
@app.route('/update/dns/<hostname>')
def fixDNS(hostname):
    result = fix_docker_dns.delay(hostname)
    return str(result.get())    # blocks until the task is finished and returns the result

def create_app():
    return app

if __name__ == '__main__':
    app.run(debug=True)
