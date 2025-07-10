from django.urls import path 
from django.shortcuts import render,redirect
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.myform, name='contact'),
    #path('portfolio/',views.portfolio_view, name='portfolio'),
    path('portfolio-details/', lambda r: render(r, 'home/portfolio-details.html'), name='portfolio-details'),
    path('service-details/', lambda r: render(r, 'home/service-details.html'), name='service-details'),
    path('starter-page/', lambda r: render(r, 'home/starter-page.html'), name='starter-page'),
]