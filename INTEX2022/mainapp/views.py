from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .funcs import searchAPI, getById, getList
from .models import MealClass, FoodItem, FoodEntry, Unit


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


def loginPageView(request) :
    return render( request, 'login.html')

def profilePageView(request) :
    return render( request, 'profile.html')

def createuserPageView(request) :
    return render( request, 'createuser.html')

def dashboardPageView(request) :
    return render( request, 'dashboard.html')

def navView(request):
    return render( request, 'nav.html')
