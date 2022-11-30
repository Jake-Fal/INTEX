from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .forms import GoalForm
from .models import Goal
import pandas as pd
import json
import requests

# Create your views here.
def indexPageView(request) :
    return render( request, 'index.html')

def journalPageView(request) :
    return render( request, 'journal.html')

def loginPageView(request) :
    return render( request, 'login.html')

def profilePageView(request) :
    return render( request, 'profile.html')

def createuserPageView(request) :
    return render( request, 'createuser.html')

def dashboardPageView(request):
    k=Goal()
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
         form = GoalForm(request.POST)
         if form.is_valid():
             form.save()
             return redirect('/')
    else:
         form = GoalForm()
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