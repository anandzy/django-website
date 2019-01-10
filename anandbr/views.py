from django.shortcuts import render

#from django.http import HttpResponse

#def index(request):
    #return HttpResponse("Hello Blog")

import requests

import json




from . models import Contact

# Create your views here.

def index(request):
    if request.method == 'POST':
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')

        r = requests.get('http://api.icndb.com/jokes/random?firstName=' + firstname + '&lastName=' + lastname)
        json_data = json.loads(r.text)
        joke = json_data.get('value').get('joke')

        context = {'joker': joke}
        return render(request, 'anandbr/index.html', context)
    else:
        firstname = 'Anand'
        lastname = 'Bhupathiraju'

        r = requests.get('http://api.icndb.com/jokes/random?firstName=' + firstname + '&lastName=' + lastname)
        json_data = json.loads(r.text)
        joke = json_data.get('value').get('joke')

        context = {'joker': joke}
        return render(request, 'anandbr/index.html', context)

def portfolio(request):
    return render(request, 'anandbr/portfolio.html')

def contact(request):
    if request.method == 'POST':
        email_r = request.POST.get('email')
        subject_r = request.POST.get('subject')
        message_r = request.POST.get('message')

        c = Contact(email=email_r, subject=subject_r, message=message_r)
        c.save()

        return render(request, 'anandbr/thank.html')
    else:
        return render(request, 'anandbr/contact.html')

#What is render?
#It will removes the syntext in index and gives usefu;; body to user

#This is from the anandbr app

'''

import json

import requests
from django.shortcuts import render

from .models import Contact


def index(request):
    if request.method == 'POST':
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')

        r = requests.get('http://api.icndb.com/jokes/random?firstName=' + firstname + '&lastName=' + lastname)
        json_data = json.loads(r.text)
        joke = json_data.get('value').get('joke')

        context = {'joker': joke}
        return render(request, 'anandbr/index.html', context)
    else:
        firstname = 'Attreya'
        lastname = 'Bhatt'

        r = requests.get('http://api.icndb.com/jokes/random?firstName=' + firstname + '&lastName=' + lastname)
        json_data = json.loads(r.text)
        joke = json_data.get('value').get('joke')

        context = {'joker': joke}
        return render(request, 'anandbr/index.html', context)


def portfolio(request):
    return render(request, 'anandbr/portfolio.html')


def contact(request):
    if request.method == 'POST':
        email_r = request.POST.get('email')
        subject_r = request.POST.get('subject')
        message_r = request.POST.get('message')

        c = Contact(email=email_r, subject=subject_r, message=message_r)
        c.save()

        return render(request, 'anandbr/thank.html')
    else:
        return render(request, 'anandbr/contact.html')
    
    '''