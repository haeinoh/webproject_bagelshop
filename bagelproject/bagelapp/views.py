from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template import Template, Context
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *

def index(request):
    if request.method == 'POST':
        form = SuggestionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            submit = form.cleaned_data['suggestion']
            suggest = Suggestion(suggestion=submit)
            suggest.save()
            form = SuggestionForm()
            #return redirect('suggestions')
        else:
            submit = ""
    else:
        form = SuggestionForm()
        submit = ""
    suggestions = Suggestion.objects.all()
    context = {
        'title':"Home",
        'content': suggestions,
        'form':form,
        'submit':submit
        }
    return render(request,'home.html',context)

@csrf_exempt
def suggestions(request):
    if request.method == 'GET':
        suggestions = Suggestion.objects.all()
        suggest = {}
        suggest['suggestions']=[]
        for suggestion in suggestions:
            suggest['suggestions']+=[{
                'id':suggestion.id,
                'suggestion': suggestion.suggestion
                }]
        return JsonResponse(suggest)
    if request.method == 'POST':
        return HttpResponse("POST successful")
    return HttpResponse("404")

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

def menu(request):
    if request.method='POST':
        form = menu_form(request.POST)
        if form.is_valid():
            form.save(request)
            return HttpResponseRedirect('/')
        else:
            form = menu_form()
        context={
            'form':form
        }
        return render(request,'menu.html',context)
