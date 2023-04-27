from django import forms
from .models import Email,DraftEmail

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['email_address','subject','body']
