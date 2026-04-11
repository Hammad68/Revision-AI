from celery import Celery

celery_instance = Celery(
    "revision_ai_tasks",
    broker="redis://localhost:6379/0",  # Redis broker URL
    backend="redis://localhost:6379/0"   # Redis backend URL for storing results
)