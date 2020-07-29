from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    char = list("abcdefghigklmnopqrstuvwxyz")
    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        char.extend("ABCDEFGHIJKLMNOPQRSTUVWQYZ")
    if request.GET.get('number'):
        char.extend("1234567890")
    if request.GET.get('special'):
        char.extend("!@#$%^&*()_+")

    thepassword = ""
    for i in range(length):
        thepassword += random.choice(char)
    return render(request, 'generator/password.html', {"thepassword": thepassword})


def aboutme(request):
    return render(request, "generator/aboutme.html")
