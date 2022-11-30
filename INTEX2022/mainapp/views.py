from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from .forms import ActualsForm
from .models import Actuals
import pandas as pd
import psycopg2
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


def dashboardPageView2(request) :
    return render( request, 'dashboard.html')

def dashboardPageView(request):
    data = {}
    context = {
         'data': data,
     }
    try:
        connection = psycopg2.connect(user="postgres",
                                    password="Broncos2025",
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
        "Protien_g": float(row[7]),
        "M_Water_L": float(row[8]),
        "F_Water_L": float(row[9])
        }
    
            



    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
    data.update(newvals)
    print(data)
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

