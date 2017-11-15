from django.contrib.auth.models import User
from django import forms
from .models import *


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'email', 'password']
			
		



class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email", "username", "password"]


class LoginForm(forms.Form):
    username = forms.CharField(label='usrbnm')
    password = forms.CharField(label='pswrd', widget=forms.PasswordInput)