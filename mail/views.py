from django.shortcuts import render
from django.core.mail import send_mail,get_connection,EmailMessage
from .forms import EmailForm
from .models import DraftEmail
from .templates import *
import imaplib
import email
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import smtplib
import email
from email.message import EmailMessage
from django.core.mail.backends.smtp import EmailBackend
import speech_recognition as sr
import pyttsx3

# Initialize the speech recognition engine
r = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def send_email(request):
    if request.method == 'POST' or request.method == 'GET':
        form = EmailForm(request.POST)
        if form.is_valid():
            email_address = form.cleaned_data['email_address']
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['subject']

            send_mail(
                subject=subject,
                message=body,
                from_email="demojanaki123@gmail.com",
                recipient_list=[email_address],
                fail_silently=False,
            )

            return render(request, 'email_sent.html')
    else:
        form = EmailForm()

    return render(request, 'sender_email.html', {'form': form})


def read_email(request):
    # Connect to the mail server
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login('demojanaki123@gmail.com', 'pohptzlscxiaddep')
    mail.select('inbox')

    # Search for the latest emails
    result, data = mail.search(None, 'ALL')
    email_ids = data[0].split()[-10:]  # get the 10 latest emails

    emails = []
    for email_id in email_ids:
        # Fetch the email
        result, data = mail.fetch(email_id, "(RFC822)")

        # Parse the email
        raw_email = data[0][1]
        raw_email_string = raw_email.decode('utf-8')
        # raw_email_string now contains the entire email message

        # Add the email to the list of emails
        emails.append(raw_email_string)

    # Close the connection to the mail server
    mail.close()
    mail.logout()

    context = {'emails': emails}
    return render(request, 'read_mail.html', context)


def automate_with_voice(request):
    if request.method == 'POST':
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)

            try:
                text = r.recognize_google(audio)
                print("Recognized speech:", text)
                engine.say("Recognized speech: " + text)
                engine.runAndWait()
            except sr.UnknownValueError:
                print("Speech recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return render(request, 'automate_with_voice.html')
