from django.urls import path

from . import views


urlpatterns = [
    #path('', views.index,),
    path('', views.index, name='home'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('contact', views.contact, name='contact'),
]

#refer views.py for the functionality defined

#The below lines are for creating and redirecting the urls

#This file is newly create after the anandbr-app created in the mywebsite project

#path('', views.index, name='home'),
# path('portfolio', views.portfolio, name='portfolio'),
# path('contact', views.contact, name='contact'),
