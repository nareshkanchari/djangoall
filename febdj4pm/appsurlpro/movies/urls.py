from django.conf.urls import url
from movies import views

urlpatterns=[
    url(r'^bb1/',views.bb1),
    url(r'^bb2/',views.bb2),
    url(r'^bb3/',views.bb3)
]