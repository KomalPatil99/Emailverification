from django import forms
from .models import *

class RegistrationForm(forms.Form):
    class Meta:
        model = Registration
        fields = ('uname','email')