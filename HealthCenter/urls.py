from django.urls import path
from .views import *



urlpatterns = [
    path('',view_base),
    path('home/',view_home, name='home'),
    path('about/',view_about, name='about'),
    path('doctors/',view_doctors, name='doctors'),
    path('news/',view_news, name='news'),
    path('contact/',view_contact, name='contact'),
    path('appointment/',view_appointment, name='appointment'),
]
