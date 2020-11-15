from django.shortcuts import render

def homepage(request):
    return render(request, 'my_portfolio/homepage.html')