from django.db import models

from django.core.validators import MinLengthValidator
# Create your models here.
state_choices = (
    ('Abia', 'Abia'),
    ('Adamawa', 'Adamawa'),
    ('Akwa-Ibom', 'Akwa-Ibom'),
    ('Anambra', 'Anambra'),
    ('Bauchi', 'Bauchi'),
    ('Bayelsa', 'Bayelsa'),
    ('Benue', 'Benue'),
    ('Borno', 'Borno'),
    ('Cross-River', 'Cross-River'),
    ('Delta', 'Delta'),
    ('Ebonyi', 'Ebonyi'),
    ('Edo', 'Edo'),
    ('Ekiti', 'Ekiti'),
    ('Enugu', 'Enugu'),
    ('Gombe', 'Gombe'),
    ('Imo', 'Imo'),
    ('Jigawa', 'Jigawa'),
    ('Kaduna', 'Kaduna'),
    ('Kano', 'Kano'),
    ('Katsina', 'Katsina'),
    ('Kebbi', 'Kebbi'),
    ('Kogi', 'Kogi'),
    ('Kwara', 'Kwara'),
    ('Lagos', 'Lagos'),
    ('Nasarawa', 'Nasarawa'),
    ('Niger', 'Niger'),
    ('Ogun', 'Ogun'),
    ('Ondo', 'Ondo'),
    ('Osun', 'Osun'),
    ('Oyo', 'Oyo'),
    ('Plateau', 'Plateau'),
    ('Rivers', 'Rivers'),
    ('Sokoto', 'Sokoto'),
    ('Taraba', 'Taraba'),
    ('Yobe', 'Yobe'),
    ('Zamfara', 'Zamfara'),
    ('Abuja', 'Federal Capital Territory Abuja')
)


faculty_choices = (
        ('Arts', 'Arts'),
        ('Agriculture', 'Agriculture'),
        ('Basic Medical Sciences', 'Basic Medical Sciences'),
        ('Dentistry', 'Dentistry'),
        ('Education', 'Education'),
        ('Engineering', 'Engineering'),
        ('Environmental Sciences', 'Environmental Sciences'),
        ('Law', 'Law'),
        ('Life Sciences', 'Life Sciences'),
        ('Management Science', 'Management Science'),
        ('Pharmacy', 'Pharmacy'),
        ('Physical Science', 'Physical Science'),
        ('Social Science', 'Social Science'),
        ('College of Medicine', 'College of Medicine'),
        ('Veterinary Medicine', 'Veterinary Medicine')
)


level_choices=(
    ('100', '100 Level'),
    ('200', '200 level'),
    ('300', '300 level'),
    ('400', '400 level'),
    ('500', '500 level'),
    ('600', '600 level'),
    ('other', '> 600 level')
)
class Registration(models.Model):
    first_name = models.CharField(max_length = 150)
    middle_name = models.CharField(max_length = 150, blank=True, null=True)
    last_name = models.CharField(max_length = 150)
    email = models.EmailField()
    # state_of_Residence = models.CharField(max_length=15, choices=state_choices, default='Edo')
    faculty = models.CharField(max_length=30, choices=faculty_choices)
    department = models.CharField(max_length=150)
    level = models.CharField(max_length=30, choices=level_choices)
    # date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=11,validators=[MinLengthValidator(11)])

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"

class Contact(models.Model):
    full_name = models.CharField(max_length = 200)
    email = models.EmailField()
    message = models.TextField(max_length=2000)

    def __str__(self):
        return self.full_name