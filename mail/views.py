from django.shortcuts import render
from django.core.mail import send_mail,get_connection,EmailMessage
from .forms import EmailForm
from .templates import *

def send_email(request):
    if request.method == 'POST' or request.method == 'GET':
        form = EmailForm(request.POST)
        if form.is_valid():
            email_address = form.cleaned_data['email_address']
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['subject']



            send_mail(
                subject = subject,
                message = body,
                from_email = "janakiramankeerthivelan21@gmail.com",
                recipient_list = [email_address],
                fail_silently  = False,
            )

            return render(request,'email_sent.html')
    else:
        form = EmailForm()

    return render(request,'sender_email.html',{'form':form})

def readmail():
    connection = get_connection(host='mail.google.com', port = 587 , username = 'janakiramankeerthivelan21@gmail.com' , password = 'alishksxhsjjdcnv')
    connection.open()

    inbox = connection.folder('INBOX')
    message = inbox[-1]

    print("subject : " , message.subject)
    print("Body : " , message.body)