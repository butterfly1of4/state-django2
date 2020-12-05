from django.shortcuts import render
from .models import Capitals
# Create your views here.




def capital_list(request):
    states= Capitals.objects.all()
    capitals = Capitals.objects.all()
    return render(request, 'usacapitals/capital_list.html', {'capitals':capitals,'states':states})