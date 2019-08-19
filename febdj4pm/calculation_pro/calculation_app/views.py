from django.shortcuts import render,redirect
from django.http.response import HttpResponse
# Create your views here.
i=None
j=None

def input(request):
    return render(request,'add.html')

def output(request):
    val1=request.GET['t1']
    val2=request.GET['t2']

    global i
    global j
    i=int(val1)
    j=int(val2)

    z=request.GET['but']

    if z=='add':
        return redirect(add)

    if z=='sub':
        return redirect(sub)

    if z=='mul':
        return redirect(mul)

    if z=='div':
        return redirect(div)

def add(request):
    k=i+j
    data = 'The addition of ',i,"and",j,"is: ",k
    return HttpResponse(data)

def sub(requst):
    k=i-j
    data = "The substraction of ",i,"and",j,"is:",k
    return HttpResponse(data)

def mul(requst):
    k=i*j
    data = "The multiplication of ",i,"and",j,"is:",k
    return HttpResponse(data)

def div(requst):
    k=i/j
    data = "The division of ",i,"and",j,"is:",k
    return HttpResponse(data)

#
#
#
# A view is a python function which takes "http request", performs business logics and returns "http response"
#
# A view supports different functions to handle the incoming request
# 1.HttpResponse()
# 2.render()
# 3.redirect()
#
# 1.HttpResponse():- It is used to transfer the HttpRequest as a HttpResponse to the browser.
#
# Views.py -------->  browser
#
# 2.render():- It is used to transfer the HttpRequest to the templae file(html file).
#
# Views.py -----------> Template(html file)
#
# 3. redirect():- It is used to transfer the HttpRequest from  one view to another view
#
# View ----> View
#
# Now we will create a project to perform all arithmatic operations
#
# step1: foldername:dj6pmapril
# step2: projectname:calculation_pro
# step3: appname: calculation_app
# step4: goto view.py file and write the below code
