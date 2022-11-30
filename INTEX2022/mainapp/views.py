from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .funcs import searchAPI, getById, getList
from .models import MealClass, FoodItem, FoodEntry
from .forms import ActualsForm
from .models import Actuals
import pandas as pd


# Create your views here.
def indexPageView(request) :
    return render( request, 'index.html')

def searchFoodView(request):
    foods = []
    food = request.GET['food']
    data = FoodItem.objects.filter(FoodName__contains=food).distinct('FoodName')[:5]
    for i in data:
        foods.append({
            'name':str(i.FoodName),
            'id':i.id
        })
    context = {
        'foods':foods
    }
    return render(request, 'searchresults.html', context)

def getAPIList(request):
    getList(200)
    return HttpResponse('data')

def journalPageView(request) :
    meals = MealClass.objects.all()
    context = {
        'meals':meals,
    }
    return render( request, 'journal.html', context)

def addFoodEntry(request):
    allFoods = list(FoodItem.objects.values_list('fdic', flat=True))
    unit = list(Unit.objects.values_list('UnitName', flat=True))

    
    return HttpResponse('Added')


def displayjournalPageView(request) :
    return render( request, 'displayjournal.html')

def loginPageView(request) :
    return render( request, 'login.html')

def profilePageView(request) :
    return render( request, 'profile.html')

def createuserPageView(request) :
    return render( request, 'createuser.html')


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