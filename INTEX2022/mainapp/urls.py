from django.urls import path
from django.contrib.auth import views as auth_view
from .views import indexPageView, createuserPageView, journalPageView, loginPageView, profilePageView, navView, dashboardPageView, displayjournalPageView, validatePage

from .views import indexPageView, createuserPageView, dashboardPageView, journalPageView, loginPageView, profilePageView, navView, searchFoodView,addFoodEntry, getAPIList, profilePageView, dashboardPageView, displayjournalPageView


urlpatterns = [
    path('', indexPageView, name='index'),
    path('profile/', profilePageView, name='profile'),
    path('journal/', journalPageView, name='journal'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('createuser/', createuserPageView, name='createuser'),
    path('validate', validatePage, name='validate'),
    path('dashboard/', dashboardPageView, name='dashboard'),
    path('nav/', navView, name='nav'),
    path('journal/searchfood/', searchFoodView, name='searchfood'),
    path('addentry/', getAPIList, name='addfoodentry'),
    path('displayjournal/', displayjournalPageView, name='displayjournal')
    ]