from django.shortcuts import render
from .forms import PersonForm

def makeentry(request):
    if request.method=='POST':
        pass
    else:
        form=PersonForm()
        return render(request,'genericviews/makeentry.html',{'form':form})
