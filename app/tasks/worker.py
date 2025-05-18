import time

from celery import Celery

from app.utils.redis_cache import cache_status

celeryApp = Celery("worker", broker="redis://localhost:6379/0")

@celeryApp.task
def ProcessFile(fileId: int, filepath: str):
    cache_status(fileId, "processing")
    time.sleep(5)
    cache_status(fileId, "done")