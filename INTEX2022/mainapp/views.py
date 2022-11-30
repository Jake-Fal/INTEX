from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
import json
import requests

# Create your views here.
def indexPageView(request) :
    return render( request, 'index.html')

def journalPageView(request) :
    return render( request, 'journal.html')

def displayjournalPageView(request) :
    return render( request, 'displayjournal.html')

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