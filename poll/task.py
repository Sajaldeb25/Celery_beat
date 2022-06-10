from celery import shared_task
from time import sleep


@shared_task
def sleepy(duration):
    sleep(duration)
    return "Done from task.py"


@shared_task
def add(x, y):
    z = x + y
    print("The sum is: ", z)


