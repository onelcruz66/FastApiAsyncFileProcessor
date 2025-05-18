import time

from celery import Celery

from app.utils.redis_cache import CacheStatus

celeryApp = Celery("worker", broker="redis://localhost:6379/0")

@celeryApp.task
def ProcessFile(fileId: int, filepath: str):
    CacheStatus(fileId, "processing")
    time.sleep(5)
    CacheStatus(fileId, "done")