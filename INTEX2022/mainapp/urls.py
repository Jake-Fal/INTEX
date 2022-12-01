from django.urls import path
from .views import indexPageView, createuserPageView, journalPageView, loginPageView, profilePageView, navView, apiTest, dashboardPageView, displayjournalPageView, register
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('', indexPageView, name='index'),
    path('profile/', profilePageView, name='profile'),
    path('journal/', journalPageView, name='journal'),
    path('login/', auth_view.LoginView.as_view(template_name = 'login.html'), name='login'),
    path('createuser/', createuserPageView, name='createuser'),
    path('dashboard/', dashboardPageView, name='dashboard'),
    path('nav/', navView, name='nav'),
    path('test/', apiTest, name='test'),
    path('displayjournal/', displayjournalPageView, name='displayjournal'),
    path('register/', register, name='register')
    ]