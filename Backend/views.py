from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.http import HttpResponse
from .forms import SignUpform


def home(request):
    return render(request, 'home.html')

def signup_views(request):
    if request.method == 'POST':
        form = SignUpform(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
       
    else:
        form = SignUpform()
        
    return render(request, 'signup.html', {'form': form})