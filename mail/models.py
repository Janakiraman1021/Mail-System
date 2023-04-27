from django.db import models
from django.contrib.auth.models import User


class Email(models.Model):
    email_address = models.EmailField()
    subject = models.CharField(max_length=300)
    body = models.CharField(max_length=300)

class DraftEmail(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    recipient = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    body = models.CharField(max_length=255)