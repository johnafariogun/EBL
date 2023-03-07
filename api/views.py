from django.shortcuts import render, redirect
from .models import Registration, Contact
from .serializers import ContactSerializer, RegistrationSerializer
from rest_framework import generics
from django.http import HttpResponse
# Create your views here.

class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    


class RegistrationCreateView(generics.CreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

def home(request):
    return render(request, 'home.html')

import csv  
def getfile(request):
    # try:
    #     if request.user.is_authenticated:  
    #         response = HttpResponse(content_type='text/csv')  
    #         response['Content-Disposition'] = 'attachment; filename="file.csv"'  
    #         register = Registration.objects.all()  
    #         writer = csv.writer(response) 
    #         writer.writerow(['id', 'full_name', 'email', 'state_of_residence', 'faculty', 'department','level', 'date_of_birth', 'phone_number'])
    #         for attendees in register:
    #             full_name = f"{attendees.first_name}  {attendees.middle_name}  {attendees.last_name}"
    #             writer.writerow([attendees.id, full_name, attendees.email, attendees.state_of_Residence, attendees.faculty, attendees.department, attendees.level, attendees.date_of_birth, attendees.phone_number])  
    #         return response
    # except ValueError:
    #     redirect('/')
    # redirect('/') 
    pass