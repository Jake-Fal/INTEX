from django.shortcuts import render

# Create your views here.
def indexPageView(request) :
    return render( request, 'homepages/index.html')

def journalPageView(request) :
    return render( request, 'homepages/index.html')

def loginPageView(request) :
    return render( request, 'homepages/index.html')

def profilePageView(request) :
    return render( request, 'homepages/index.html')

def createuserPageView(request) :
    return render( request, 'homepages/index.html')

def dashboardPageView(request) :
    return render( request, 'homepages/index.html')