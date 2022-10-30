from . import views
from django.urls import path

urlpatterns=[
    path('',views.homeView,name='home'), #this is for home url
    path('search',views.searchView,name='search'), #this is the search
]