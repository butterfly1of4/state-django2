from django.shortcuts import render, redirect
from .models import Capitals
import random
# import randint
from .forms import CapitalForm
# Create your views here.


def home(request):
     return render(request, 'usacapitals/base.html')


def capital_list(request):
    states = Capitals.objects.all()
    capitals = Capitals.objects.all()
    return render(request, 'usacapitals/capital_list.html', {'capitals': capitals, 'states': states})


def match_capital(request):
     states = Capitals.objects.all()
     capitals = Capitals.objects.all()
     
     return render(request, 'usacapitals/capital_game.html')

def random_state(state):
     state = Capitals.objects.GET(state=state)
     random.choice(state)
     print(state )
     return render({'state': state})
     
     
     
     # state= Capitals.objects.order_by('state')
     # form = CapitalForm()
     # context_dict = {'form': form, 'state': state}
     # if request.method == 'POST':
     #      instance = Capitals.objects.get(id=request.POST['q_id'])
     #      form =  CapitalForm(request.POST, instance=instance)
          
     #      if form.is_valid():
     #           if request.POST.get("capital").strip() == instance.capital:
