# celery.py

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

import hello.settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hello.settings')

app = Celery('hello', worker_prefetch_multiplier=hello.settings.CELERY_WORKER_PREFETCH_MULTIPLIER)

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings', namespace='CELERY')
# app.conf.task_routes = hello.settings.CELERY_TASK_ROUTES
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
