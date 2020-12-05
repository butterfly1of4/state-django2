from django.urls import path
from . import views

urlpatterns = [
    # path('',),
    path('', views.capital_list, name='capital_list')
]