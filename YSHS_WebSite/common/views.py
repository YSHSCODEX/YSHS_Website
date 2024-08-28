from django.shortcuts import render

def signup(request):
    return render(request, 'mainPage/home.html')