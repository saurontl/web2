from django.shortcuts import render
from .models import Client

def get_clients(request):
    clients = Client.objects.all()
    return render(request, 'clients.html', {'clients': clients})
