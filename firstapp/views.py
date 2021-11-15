from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.


def djangohello(request: HttpRequest):
    return HttpResponse('Hello django')
