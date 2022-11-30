from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.shortcuts import render, redirect
#from .forms import MovieDataForm
import json
import requests

# Create your views here.
def indexPageView(request) :
    return render( request, 'index.html')

def journalPageView(request) :
    return render( request, 'journal.html')

# Login Function
def loginPageView(request) :
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        messages.info(request, "Please login.")
        return HttpResponseRedirect('/index.html')

def loginUser(request) :
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user != None:
            login(request, user)
            return HttpResponseRedirect('/profile.html')
        else: 
            messages.error(request, "Enter correct username/password")
            return HttpResponseRedirect('/index.html')

def logoutUser(request) :
    logout(request)
    request.user = None
    return HttpResponseRedirect('index.html')

def profilePageView(request) :
    return render( request, 'profile.html')

def createuserPageView(request) :
    return render( request, 'createuser.html')

# def dashboardPageView(request):
#     data = User.objects.all()
#     if request.method == 'POST':
#         form = MovieDataForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     else:
#         form = MovieDataForm()
#     context = {
#         'data': data,
#         'form': form,
#     }
#     return render(request, 'dashboard.html', context)

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