from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import ActualsForm, LoginForm
from .models import Actuals
import pandas as pd

import json
import requests
from .forms import UserForm

# Create your views here.
def indexPageView(request) :
    return render( request, 'index.html')

def journalPageView(request) :
    return render( request, 'journal.html')

def displayjournalPageView(request) :
    return render( request, 'displayjournal.html')

def loginPageView(request) :
    form = LoginForm
    return render( request, 'login.html', {'form': form})

def profilePageView(request) :
    return render( request, 'profile.html')

def register(request):
    if request.method == "POST" :
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # messages.success(request, f'Hi {username}, your account was created successfully')
            return HttpResponseRedirect('/createuser')
    else :
        form = UserCreationForm

    return render(request, 'register.html', {'form': form})

def createuserPageView(request) :
    submitted = False
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/createuser?submitted=True')
    else:
        form = UserForm
        if 'submitted' in request.GET:
            submitted = True
    form = UserForm
    return render( request, 'createuser.html', {'form': form, 'submitted':submitted})


def dashboardPageView2(request) :
    return render( request, 'dashboard.html')

def dashboardPageView(request):
    k=Actuals()
    data = {}
    for attr, value in k.__dict__.items():
        print(attr, value)
        newvals = {attr: value}
        data.update(newvals)
    #  data = {}
    #  for col in Goal:
    #     newvals = {col.iloc[0]: col.iloc[1]}
    #     data.update(newvals)
    #     print(newvals)
    #     print(data)
    
    if request.method == 'POST':
         form = ActualsForm(request.POST)
         if form.is_valid():
             form.save()
             return redirect('/')
    else:
         form = ActualsForm()
    context = {
         'data': data,
         'form': form,
     }
    return render(request, 'dashboard.html', context)

def navView(request):
    return render( request, 'nav.html')

def apiTest(request):
    nutrients = ['Protein', 'Sodium, Na', 'Potassium, K', 'Water', 'Phosphorus, P']
    foodInfo = {}
    r = requests.get('https://api.nal.usda.gov/fdc/v1/foods/search?api_key=ZG2gfG4lRbZh0UXSFos1GvXbvUrvjsdYX7kYBdVI&query=Cheddar%20Cheese')
    for i in r.json()['foods']:
        nuts = {}
        name = i['description'].lower()
        for j in i['foodNutrients']:
            if j['nutrientName'] in nutrients:
                nuts[j['nutrientName']] = j['value']
        foodInfo[name] = nuts
    print(foodInfo)
    return HttpResponse('Hello')