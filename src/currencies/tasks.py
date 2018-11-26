from __future__ import absolute_import, unicode_literals
import logging
from celery import task
from django.conf import settings


logger = logging.getLogger("celery")


@task
def show_hello_world():
    logger.info("-"*25)
    logger.info("Printing Hello from Celery")
    logger.info("-"*25)
