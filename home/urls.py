from django.urls import path

from . import views

urlpatterns = [
    path('', views.firstpage, name='firstpage'),
    path('index/', views.index, name = "index"),
    path('searchbar/', views.searchbar, name ='searchbar'),
    path('stackindex/', views.stackindex, name = 'stackindex'),
    path('stacksearchbar/', views.stacksearchbar, name = 'stacksearchbar')
]