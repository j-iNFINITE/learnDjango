from django.shortcuts import render,redirect
from django.core.context_processors import csrf
from django.contrib.auth import *
from django.contrib.auth import forms
# Create your views here.
class login(forms.forms):
    login = forms.AuthenticationForm()
def user_login(request):
    if request.POST:
        username = password = ''
        username = request.POST('username')
        password = request.POST('password')
        user = authenticate(username=username,password=password)
        if user is not None and user.is_active:
            login(request,user)
            return redirect('/')
    ctx = {}
    ctx.update(csrf(request))
    return render(request,'login.html', ctx)