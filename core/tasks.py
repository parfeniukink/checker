from config.celery import celery_app

from core.services import Checker


@celery_app.task
def generate_reports():
    checker = Checker()
    checker.generate_reports()
