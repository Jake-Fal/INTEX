from django.urls import path
from .views import indexPageView, createuserPageView, journalPageView, loginPageView, profilePageView, navView, apiTest


urlpatterns = [
    path('', indexPageView, name='index'),
    path('profile/', profilePageView, name='profile'),
    path('journal/', journalPageView, name='journal'),
    path('login/', loginPageView, name='login'),
    path('createuser/', createuserPageView, name='createuser'),
    #path('dashboard/', dashboardPageView, name='dashboard'),
    path('nav/', navView, name='nav'),
    path('test/', apiTest, name='test'),
    ]