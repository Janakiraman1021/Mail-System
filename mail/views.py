from django.shortcuts import render
from django.core.mail import send_mail,get_connection,EmailMessage
from .forms import EmailForm
from .templates import *
import imaplib
import email
from django.shortcuts import render


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





def read_email(request):
    # Connect to the Gmail IMAP server and login
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login('janakiramankeerthivelan21@gmail.com', 'alishksxhsjjdcnv')

    # Select the inbox folder and retrieve all emails
    mail.select('inbox')
    result, data = mail.uid('search', None, "ALL")
    email_uids = data[0].split()

    # Iterate through all emails and extract relevant information
    emails = []
    for uid in email_uids:
        result, email_data = mail.uid('fetch', uid, '(RFC822)')
        raw_email = email_data[0][1].decode('utf-8')
        email_message = email.message_from_string(raw_email)
        sender = email.utils.parseaddr(email_message['From'])[1]
        subject = email_message['Subject']
        body = email_message.get_payload()
        emails.append({'sender': sender, 'subject': subject, 'body': body})

    # Render the email details in a template
    return render(request, 'read_email.html', {'emails': emails})
