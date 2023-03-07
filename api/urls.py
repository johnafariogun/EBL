from django.urls import path
from .views import ContactCreateView,home, RegistrationCreateView, getfile

from django.shortcuts import render


urlpatterns = [
    path('contact', ContactCreateView.as_view()),
    path('register', RegistrationCreateView.as_view()),
    path('export', getfile),
    path("", home)
]