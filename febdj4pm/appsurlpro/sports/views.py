from django.shortcuts import render
from django.http.response import HttpResponse

def cricket(request):
    cricket="next world cup in 2020"
    return HttpResponse(cricket)
def hockey(request):
    hockey='This is our national game'
    return HttpResponse(hockey)
def football(request):
    football='This is an international game'
    return HttpResponse(football)