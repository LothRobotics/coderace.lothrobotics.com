from django.shortcuts import render
from lobbies.models import Lobby

# Create your views here.

context = {}
context['lobbies'] = list(Lobby.objects.all())

def index(request):
    context['lobbies'] = list(Lobby.objects.all())
    return render(request, 'lobbies.html', context)

def lobby(request):
    return render(request, 'home.html')