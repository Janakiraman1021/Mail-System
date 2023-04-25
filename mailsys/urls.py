from django.contrib import admin
from django.urls import path
from mail.views import send_email,read_email



urlpatterns = [
    path("admin/", admin.site.urls),
    path('send_email/',send_email,name='send_email'),
    path('read/',read_email,name='read_email'),
]
