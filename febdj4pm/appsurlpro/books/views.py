from django.shortcuts import render
from django.http.response import HttpResponse

def python(request):
    python="<h1>Python is powerfull and simple programing language</h1>"
    return HttpResponse(python)
def django(request):
    django="<h2>Django is powerfull framework</h2>"
    return HttpResponse(django)
def restapi(request):
    ra="<h3>communicator between two apps</h3>"
    return HttpResponse(ra)