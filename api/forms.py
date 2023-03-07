from .models import Registration, Contact
from django import forms

class RegistrationForm(forms.ModelForm):
    """Form definition for Registration."""

    class Meta:
        """Meta definition for Registrationform."""

        model = Registration
        fields = '__all__'


class ContactForm(forms.ModelForm):
    """Form definition for ContactModel."""

    class Meta:
        """Meta definition for Contactform."""

        model = Contact
        fields = '__all__'

