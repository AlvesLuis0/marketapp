from django.shortcuts import render
from .controller import clientController

# Create your views here.
def login(request):
  return render(request, "login.html")

def register(request):
  return render(request, "register.html")

createClient = clientController.createClient
clientView = clientController.clientView