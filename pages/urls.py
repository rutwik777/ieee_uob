from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,  name='home'),  #Home page Local Host
    path('/events', views.events,  name='events'),
]