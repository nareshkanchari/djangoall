from django.shortcuts import render
from django.http.response import HttpResponse

def poly(request):
    poly="worst polytics"
    return HttpResponse(poly)
def crime(request):
    crime="from last 2years crime has redused stated by the Hyderabad Police Comistionar"
    return HttpResponse(crime)
def entertainment(request):
    entertainment="shahid kapoor commited two projects and heroin also same for two projects she is deepika padukone"
    return HttpResponse(entertainment)
