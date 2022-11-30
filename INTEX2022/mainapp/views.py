from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .funcs import callAPI
from .models import MealClass


# Create your views here.
def indexPageView(request) :
    return render( request, 'index.html')

def searchFoodView(request):
    foods = []
    food = request.GET['food']
    data = callAPI(food)
    for i in data:
        foods.append({
            'name':i['name'],
            'id':i['id']
        })
    context = {
        'foods':foods
    }
    return render(request, 'searchresults.html', context)

def journalPageView(request) :
    meals = MealClass.objects.all()
    context = {
        'meals':meals,
    }
    return render( request, 'journal.html', context)

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
