from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template import Template, Context
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from carton.cart import Cart

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
            # process the data in form.cleaned_data as required
            form = SuggestionForm()
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

def products(request):
    products = productform.objects.all
    context = {
        'title':'Product',
    }
    return render(request, 'menu.html', context)

def custom(request):
    if request.method == 'POST':
        form = custom_form(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password1')
            )
            login(request,user)
            return HttpResponseRedirect('/')
    else:
        form = custom_form()
    context = {
        'title':'Custom_recipe',
        'form':form
    }
    return render(request,'custom.html', context)

def orders(request):
    if request.method == 'POST':
        form = order_form(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password1')
            )
            login(request,user)
            return HttpResponseRedirect('/')
    else:
        form = order_form()
    context = {
        'title':'Order',
        'form':form
    }
    return render(request, 'order.html', context)
#Cart
def show(request):
    cart = Cart(request.session)
    response = ''
    for item in cart.items:
        response += '%(quantity)s %(item)s for $%(price)s\n' % {
            'quantity': item.quantity,
            'item': item.product.name,
            'price': item.subtotal,
        }
        response += 'items count: %s\n' % cart.count
        response += 'unique count: %s\n' % cart.unique_count
    return HttpResponse(response)

def add(request):
    cart = Cart(request.session)
    product = Product.objects.get(pk=request.POST.get('product_id'))
    quantity = request.POST.get('quantity', 1)
    discount = request.POST.get('discount', 0)
    price = product.price - float(discount)
    cart.add(product, price, quantity)
    return HttpResponse()

def remove(request):
    cart = Cart(request.session)
    product = Product.objects.get(pk=request.POST.get('product_id'))
    cart.remove(product)
    return HttpResponse()

def remove_single(request):
    cart = Cart(request.session)
    product = Product.objects.get(pk=request.POST.get('product_id'))
    cart.remove_single(product)
    return HttpResponse()

def clear(request):
    cart = Cart(request.session)
    cart.clear()
    return HttpResponse()

def set_quantity(request):
    cart = Cart(request.session)
    product = Product.objects.get(pk=request.POST.get('product_id'))
    quantity = request.POST.get('quantity')
    cart.set_quantity(product, quantity)
    return HttpResponse()
#Register
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
