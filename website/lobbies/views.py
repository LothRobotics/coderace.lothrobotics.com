from django.shortcuts import render, redirect
from lobbies.models import Lobby
from time import sleep
import multiprocessing

# Create your views here.

context = {}
context['lobbies'] = list(Lobby.objects.all())
context['room-name'] = 'broadcast'


def index(request):
    context['lobbies'] = list(Lobby.objects.all())
    return render(request, 'lobbies.html', context)
    

def lobby(request):
    return render(request, 'home.html')