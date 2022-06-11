from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')


def password(request):

    characters = list('qwertyuiopasdfghjklzxcvbnm')

    lenght = int(request.GET.get('lenght', 12))

    if request.GET.get('uppercase'):
        characters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&**()_+'))

    if request.GET.get('numbers'):
        characters.extend(list('123654789'))

    thepassword = ''
    for x in range(lenght):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})

# Create your views here.
