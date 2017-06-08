from django import forms
from django.contrib.auth.forms import User
from .forms import *
from .models import *


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


