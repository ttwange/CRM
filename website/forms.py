from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput())
    first_name = forms.CharField(label=,)
    last_name = forms.CharField(label=)

