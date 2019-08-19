from django.conf.urls import url
from sports import views

urlpatterns=[
    url(r'^cricket/',views.cricket),
    url(r'^hockey/',views.hockey),
    url(r'^fb/',views.football)
]