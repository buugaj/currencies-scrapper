from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
import logging
logger = logging.getLogger("Celery")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('mydjango')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
app.send_task('currencies.tasks.scrap_currencies')

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


