from django.conf.urls import url
from news import views

urlpatterns=[
    url(r'^poly/',views.poly),
    url(r'^crime/',views.crime),
    url(r'^enter/',views.entertainment)
]