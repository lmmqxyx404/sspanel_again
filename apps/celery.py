# main task is to expose app
import os

from celery import Celery

from configs.default.cron import task_schedule

# set the default Django settings module for the 'celery' program.
# todo: 1. complete the configs module.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "configs")

# 2. 
app = Celery("sspanel")
