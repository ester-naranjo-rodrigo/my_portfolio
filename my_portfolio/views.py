from django.shortcuts import render
import datetime

def homepage(request):
    return render(request, 'my_portfolio/homepage.html')