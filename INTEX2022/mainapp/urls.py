from django.urls import path
from .views import indexPageView, createuserPageView, journalPageView, loginPageView, profilePageView, navView, apiTest, loginUser, logoutUser


urlpatterns = [
    path('', indexPageView, name='index'),
    path('profile/', profilePageView, name='profile'),
    path('journal/', journalPageView, name='journal'),
    path('login/', loginPageView, name='login'),
    path('login_user', loginUser, name='login_user'),
    path('logout/', logoutUser, name='logout'),
    path('createuser/', createuserPageView, name='createuser'),
    #path('dashboard/', dashboardPageView, name='dashboard'),
    path('nav/', navView, name='nav'),
    path('test/', apiTest, name='test'),
    ]