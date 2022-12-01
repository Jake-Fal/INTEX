from django import views
from django.urls import path
from django.contrib.auth import views as auth_view
from .views import indexPageView, createuserPageView, journalPageView, loginPageView, profilePageView, navView, dashboardPageView, displayjournalPageView, validatePage, register, addFoodItem
from django.contrib.auth import views as auth_view
from .views import indexPageView, createuserPageView, dashboardPageView, journalPageView, loginPageView, profilePageView, navView, searchFoodView,addFoodEntry, getAPIList, profilePageView, dashboardPageView, displayjournalPageView, submitFoodItem, addWaterEntry, submitWaterEntry, editWaterEntry, deleteWaterEntry


urlpatterns = [
    path('', indexPageView, name='index'),
    path('profile/', profilePageView, name='profile'),
    path('journal/', journalPageView, name='journal'),
    path('login/', auth_view.LoginView.as_view(template_name = 'login.html'), name='login'),
    path('createuser/', createuserPageView, name='createuser'),
    path('validate/', validatePage, name='validate'),
    path('dashboard/', dashboardPageView, name='dashboard'),
    path('nav/', navView, name='nav'),
    path('journal/searchfood/', searchFoodView, name='searchfood'),
    path('addentry/', addFoodEntry, name='addfoodentry'),
    path('displayjournal/', displayjournalPageView, name='displayjournal'),
    path('register/', register, name='register'),
    path('addfood/', addFoodItem, name='addfood'),
    path('submitfood/', submitFoodItem, name='submitfood'),
    path('addwater/', addWaterEntry, name='addwater'),
    path('submitwater/', submitWaterEntry, name='submitwater'),
    path('editwater/<int:id>/', editWaterEntry, name='editwater'),
    path('deletewater/<int:id>/', deleteWaterEntry, name='deletewater')
    ]