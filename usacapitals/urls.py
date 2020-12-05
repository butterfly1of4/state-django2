from django.urls import path
from . import views

urlpatterns = [
    path('', views.capital_list, name='capital_list')
]