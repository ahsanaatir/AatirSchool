from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth import logout
from .forms import *
from django.shortcuts import render
from .models import *
import json
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy




def index(request):
    return render(request, 'school/index.html')

def dashboard(request):
    return render(request, 'school/dashboard.html')



def logout_user(request):
        logout(request)
        form = UserForm(request.POST or None)
        context = {
            "form": form,
        }
        return render(request, 'school/login.html', context)


# login user
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # albums = Album.objects.filter(user=request.user)
                return render(request, 'school/index.html')
            else:
                return render(request, 'school/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'school/login.html', {'error_message': 'Invalid login'})
    return render(request, 'school/login.html')




# register
def signup(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # albums = Album.objects.filter(user=request.user)
                return render(request, 'school/index.html')
    context = {
        "form": form,
    }
    return render(request, 'school/signup.html', context)

