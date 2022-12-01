from django.urls import path
from django.contrib.auth import views as auth_view
from .views import indexPageView, createuserPageView, journalPageView, profilePageView, navView, dashboardPageView, displayjournalPageView, register
from django.contrib.auth import views as auth_view
from .views import indexPageView, createuserPageView, dashboardPageView, journalPageView, profilePageView, navView, searchFoodView,addFoodEntry, getAPIList, profilePageView, dashboardPageView, displayjournalPageView


urlpatterns = [
    path('', indexPageView, name='index'),
    path('profile/', profilePageView, name='profile'),
    path('journal/', journalPageView, name='journal'),
    path('login/', auth_view.LoginView.as_view(template_name = 'login.html'), name='login'),
    path('createuser/', createuserPageView, name='createuser'),
    path('dashboard/', dashboardPageView, name='dashboard'),
    path('nav/', navView, name='nav'),
    path('journal/searchfood/', searchFoodView, name='searchfood'),
    path('addentry/', getAPIList, name='addfoodentry'),
    path('displayjournal/', displayjournalPageView, name='displayjournal'),
    path('register/', register, name='register')
    ]
    