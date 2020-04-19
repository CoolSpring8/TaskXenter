from celery import Celery

celery_app = Celery("worker", backend='rpc://guest@queue', broker="amqp://guest@queue//")

celery_app.conf.task_routes = {"app.worker.test_celery": "main-queue"}
celery_app.conf.timezone='Asia/Shanghai'
