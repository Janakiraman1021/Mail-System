from django.db import models

class Email(models.Model):
    email_address = models.EmailField()
    subject = models.CharField(max_length=300)
    body = models.CharField(max_length=300)