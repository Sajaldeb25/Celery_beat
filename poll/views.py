from django.http import HttpResponse
from .task import sleepy, add


def index(request):
    sleepy.delay(20)
    return HttpResponse("Hello, world. You're at the polls index. Sajal")



