from django import forms
from .models import Email,DraftEmail

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['email_address','subject','body']

from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
