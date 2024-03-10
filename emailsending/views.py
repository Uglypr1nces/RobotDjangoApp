from django.shortcuts import render
from django.http import HttpResponse
from .python_functions.emailsender import *
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

def Contact(request):
    return render(request, 'contact.html')

def index(requet):
    return render(request, 'base.html')
    
def send_email(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        self_email = "unattractivequeen@gmail.com"
        email = data.get('reciever_email')
        subject = data.get('subject')
        message = data.get('message')
        print(f'Email sent from {self_email} to {email} with subject {subject} and message {message}')
        try:
            send(self_email,email, subject, message)
        except:
            return HttpResponse('Email Not Sent, Please check your credentials and try again.')
        return HttpResponse('Email Sent')
