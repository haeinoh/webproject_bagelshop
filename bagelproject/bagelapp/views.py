from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template import Template, Context
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *

def index(request):
    context = {
        'title':"Home",
    }
    return render(request,'home.html',context)

def register(request):
    if request.method == 'POST':
        form = registration_form(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password1')
            )
            login(request,user)
            return HttpResponseRedirect('/')
    else:
        form = registration_form()
    context = {
        'title':'Register',
        'form':form
    }
    return render(request, 'register.html', context)
