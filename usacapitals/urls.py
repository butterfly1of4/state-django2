from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('capitals/', views.capital_list, name='capital_list'),
    path('game/', views.match_capital, name='match_capital')
]