from django.urls import path
from . import views


urlpatterns = [
    path('web', views.web, name = 'web'),
    path('login', views.login, name = 'login'),
    path('sign', views.sign, name = 'sign'),
    path('logout', views.logout, name = 'logout'),
    path('save', views.save, name= 'save'),
   
]