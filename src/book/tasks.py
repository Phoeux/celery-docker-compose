from celery import shared_task
from time import sleep


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def sleep_task(pause):
	sleep(pause)
	return f'hello world {pause}'