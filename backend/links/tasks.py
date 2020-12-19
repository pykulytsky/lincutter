from celery import Celery
from config.celery import app

from .models import Link
from datetime import datetime, timedelta

@app.task
def delete_link(payload):
    try:
        Link.objects.get(truncated_link_uuid=payload).delete()
    except Link.DoesNotExist:
        raise ValueError("Link already deleted")
