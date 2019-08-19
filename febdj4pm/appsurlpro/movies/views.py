from django.shortcuts import render
from django.http.response import HttpResponse

def bb1(request):
    bb1="This is a nice movie"
    return HttpResponse(bb1)
def bb2(request):
    bb2="This is an animation wonder"
    return HttpResponse(bb2)
def bb3(request):
    bb3='Upcoming movie'
    return HttpResponse(bb3)
