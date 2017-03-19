from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import Template, Context
from django.views.decorators.csrf import csrf_exempt

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
            # process the data in form.cleaned_data as required
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
