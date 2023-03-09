from django.urls import path
from .views import ContactCreateView,home, RegistrationCreateView, getfile



urlpatterns = [
    path('contact', ContactCreateView.as_view(), name='contact'),
    path('register', RegistrationCreateView.as_view(), name='register'),
    #path('export', getfile),
    path("", home)
]
