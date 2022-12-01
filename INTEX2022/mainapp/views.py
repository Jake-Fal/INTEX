from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .funcs import searchAPI, getById, getList
from .models import MealClass, FoodItem, FoodEntry, WaterEntry, UserInfo
from .models import Actuals
from .forms import LoginForm

import pandas as pd
import psycopg2
import json
import requests
from .forms import UserForm



# Create your views here.
def indexPageView(request) :
    
    userid = request.user.id
    print(userid)
    return render( request, 'index.html', {'id':userid})

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

def addFoodItem(request):
    return render(request, 'addfood.html')

def submitFoodItem(request):
    if request.method == 'POST':
        name = request.POST['name'].lower()
        sodium = request.POST['sodium']
        potassium = request.POST['potassium']
        phosphorus = request.POST['phosphorus']
        protein = request.POST['protein']

        food = FoodItem()
        food.FoodName = name
        food.Protein_g = protein
        food.Sodium_mg = sodium
        food.Potassium_mg = potassium
        food.Phosphate_mg = phosphorus
        food.save()

    return redirect(journalPageView)

def addFoodEntry(request):
    if request.method == 'POST':
        user = request.POST['userID']
        date = request.POST['EntryDate']
        meal = request.POST['meal']
        food = request.POST['foodID']
        servings = request.POST['servings']
    return HttpResponse('Added')

def addWaterEntry(request):
    return render(request, 'addwaterentry.html')

def submitWaterEntry(request):
    if request.method == 'POST':
        userid = request.POST['userid']
        date = request.POST['EntryDate']
        amount = request.POST['amount']

        waterEntry = WaterEntry()
        waterEntry.UserID = UserInfo.objects.get(id=userid)
        waterEntry.DateTime = date
        waterEntry.Amount = amount
        waterEntry.save()
    return redirect(displayjournalPageView)

def editWaterEntry(request, id):
    pass

def deleteWaterEntry(request, id):
    WaterEntry.objects.get(id=id, UserID=request.user.id).delete()
    return redirect(displayjournalPageView)

def getAPIList(request):
    #getList(200)
    return HttpResponse('data')

def journalPageView(request) :
    meals = MealClass.objects.all()
    data = {}
    pdata = {}
    newvals = {}
    npvals = {}
    pkeys = []
    pvals = []
    keys = []
    values = []
    context = {
         'keys': keys,
         'values': values,
         'data': data,
         'pvals': pvals,
         'pkeys': pkeys,
         'meals': meals
     }
    try:
        connection = psycopg2.connect(user="postgres",
                                    password="Andyman72599",
                                    host="localhost",
                                    port="5432",
                                    database="kidney_health")
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from mainapp_goal"

        cursor.execute(postgreSQL_select_Query)
        print("Selecting rows from mobile table using cursor.fetchall")
        mobile_records = cursor.fetchall()

        print("Print each row and it's columns values")

        for row in mobile_records:
            print("Id = ", row[0], )
            print("Min_Sodium_mg = ", row[1])
            print("Max_Sodium_mg  = ", row[2])
            print("Min_Potassium_mg  = ", row[3])
            print("Max_Potassium_mg  = ", row[4])
            print("Min_Phosphorous_mg  = ", row[5])
            print("Max_Phosphorous_mg  = ", row[6])
            print("Protien_g  = ", row[7])
            print("M_Water_L  = ", row[8])
            print("F_Water_L  = ", row[9])

        newvals = {'Min_Sodium_mg': row[1], 
        "Max_Sodium_mg": row[2],
        "Min_Potassium_mg": row[3],
        "Max_Potassium_mg": row[4],
        "Min_Phosphorous_mg": row[5],
        "Max_Phosphorous_mg": row[6],
        }

        npvals = {"Protien_g": float(row[7]),
        "M_Water_L": float(row[8]),
        "F_Water_L": float(row[9])}
    
            



    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
    data.update(newvals)
    pdata.update(npvals)
    for key, value in data.items():
        keys.append(key)
        values.append(value)
    for key, value in pdata.items():
        pkeys.append(key)
        pvals.append(value)

    return render(request, 'journal.html', context)

def displayjournalPageView(request) :
    waterEntries = WaterEntry.objects.all().values()
    context = {
        'water':waterEntries
    }
    print(waterEntries)
    return render( request, 'displayjournal.html', context)


def profilePageView(request) :
    UserInfo.objects.get(user = request.user.id).id
    obj = get_object_or_404(UserInfo, pk = UserInfo.objects.get(user = request.user.id).id)
    form = UserForm(request.POST or None, instance = obj)

    # if form.is_valid:
    #     form.save()
    return render( request, 'profile.html', {'form':form})

def updateProfile(request):
    UserInfo.objects.get(user = request.user.id).id
    obj = get_object_or_404(UserInfo, pk = UserInfo.objects.get(user = request.user.id).id)
    userinfo = obj
    if request.method == 'POST':
        FirstName = request.POST['FirstName']
        LastName = request.POST['LastName']
        DOB = request.POST['DOB']
        HeightFt = request.POST['HeightFt']
        HeightIn = request.POST['HeightIn']
        Weight = request.POST['Weight']
        Sex = request.POST['Sex']

        userinfo.FirstName = FirstName
        userinfo.LastName = LastName
        userinfo.DOB = DOB
        userinfo.HeightFt = HeightFt
        userinfo.HeightIn = HeightIn
        userinfo.Weight = Weight
        userinfo.Sex = Sex

        userinfo.save()
    return redirect(profilePageView)

def register(request):
    if request.method == "POST" :
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
            # print(request.session['_auth_user_id'])
            # username = form.cleaned_data.get('username')
            # messages.success(request, f'Hi {username}, your account was created successfully')
            return HttpResponseRedirect('/login/')
    else :
        form = UserCreationForm

    return render(request, 'register.html', {'form': form})

def createuserPageView(request) :
    submitted = False
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            actualsEntry = Actuals()
            actualsEntry.UserID = UserInfo.objects.get(user = request.user.id)
            actualsEntry.Protein_g = 0
            actualsEntry.Sodium_mg = 0
            actualsEntry.Phosphorous_mg = 0
            actualsEntry.Potassium_mg = 0
            actualsEntry.Water_L = 0
            actualsEntry.save()
            return HttpResponseRedirect('/profile/')
    else:
        form = UserForm
        if 'submitted' in request.GET:
            submitted = True
    form = UserForm
    return render( request, 'createuser.html', {'form': form, 'submitted':submitted})

def login_redirect(request) :
    try:
        if UserInfo.objects.get(user = request.user.id) :
            return HttpResponseRedirect('/journal/')
    except :
        return HttpResponseRedirect('/createuser/')

def dashboardPageView2(request) :
    return render( request, 'dashboard.html')

def dashboardPageView(request):
    data = {}
    pdata = {}
    newvals = {}
    npvals = {}
    pkeys = []
    pvals = []
    keys = []
    values = []
    context = {
         'keys': keys,
         'values': values,
         'data': data,
         'pvals': pvals,
         'pkeys': pkeys

     }
    try:
        connection = psycopg2.connect(user="postgres",
                                    password="Andyman72599",
                                    host="localhost",
                                    port="5432",
                                    database="kidney_health")
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from mainapp_goal"

        cursor.execute(postgreSQL_select_Query)
        print("Selecting rows from mobile table using cursor.fetchall")
        mobile_records = cursor.fetchall()

        print("Print each row and it's columns values")

        for row in mobile_records:
            print("Id = ", row[0], )
            print("Min_Sodium_mg = ", row[1])
            print("Max_Sodium_mg  = ", row[2])
            print("Min_Potassium_mg  = ", row[3])
            print("Max_Potassium_mg  = ", row[4])
            print("Min_Phosphorous_mg  = ", row[5])
            print("Max_Phosphorous_mg  = ", row[6])
            print("Protien_g  = ", row[7])
            print("M_Water_L  = ", row[8])
            print("F_Water_L  = ", row[9])

        newvals = {'Min_Sodium_mg': row[1], 
        "Max_Sodium_mg": row[2],
        "Min_Potassium_mg": row[3],
        "Max_Potassium_mg": row[4],
        "Min_Phosphorous_mg": row[5],
        "Max_Phosphorous_mg": row[6],
        }

        npvals = {"Protien_g": float(row[7]),
        "M_Water_L": float(row[8]),
        "F_Water_L": float(row[9])}
    
            



    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
    data.update(newvals)
    pdata.update(npvals)
    for key, value in data.items():
        keys.append(key)
        values.append(value)
    for key, value in pdata.items():
        pkeys.append(key)
        pvals.append(value)

    return render(request, 'dashboard.html', context)

def navView(request):
    return render( request, 'nav.html')

