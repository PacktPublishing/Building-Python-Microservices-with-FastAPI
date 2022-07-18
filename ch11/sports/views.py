from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse

def view_index(req: HttpRequest):
    return HttpResponse(content="django integration")
