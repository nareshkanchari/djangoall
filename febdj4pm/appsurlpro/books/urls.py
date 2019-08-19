from django.conf.urls import url
from books import views

urlpatterns=[
    url(r'^python/',views.python),
    url(r'^django/',views.django),
    url(r'^ra/',views.restapi)
]