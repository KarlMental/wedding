from django import forms
from .models import Guest

class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['name', 'rsvp_answer', 'email', 'dietary_restrictions', 'shuttle']