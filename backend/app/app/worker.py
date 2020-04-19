import os
import sentry_sdk
import httpx
from celery.schedules import crontab

from app.core.celery_app import celery_app

sentry_sdk.init(os.environ['SENTRY_DSN'])


@celery_app.on_after_configure.connect
def add_periodic(hour, minute, day, method, url, data, success_result, **kwargs):
    celery.add_periodic_task({'hour': hour, 'minute': minute, 'day': day}, hit_url.s(
        method, url, data, success_result))


@celery_app.task(acks_late=True)
def hit_url(method, url, data, success_result):
    try:
        if method == 'post':
            r = httpx.post(url=url, data=data)
        else:
            r = httpx.get(url=url)
        if success_result in r.text():
            return 'Succeeded'
    except:
        pass
    return 'failed'
