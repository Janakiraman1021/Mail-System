from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mail.views import send_email, read_email, automate_with_voice, main, login

urlpatterns = [
    path("", main, name='main'),
    path("login/", login, name='login'),
    path("admin/", admin.site.urls),
    path('send_email/', send_email, name='send_email'),
    path('read/', read_email, name='read_email'),
    path('automatic/', automate_with_voice, name='automate_with_voice'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
