from django import forms
from .models import Password

class PasswordForm(forms.ModelForm):
    class Meta:
        model = Password
        fields = ['password_length']
        labels = {'password' : 'Password length'}
