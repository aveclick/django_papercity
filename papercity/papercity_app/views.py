from django.http import request
from django.shortcuts import render



def home(request):
    return render(request, 'papercity_app/home.html')

def book_list(request):
    return render(request, 'papercity_app/book_list.html')

