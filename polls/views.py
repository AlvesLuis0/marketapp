from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone

from .models import CLIENT, PRODUCT

# Create your views here.
def index(request):
  return render(request, "index.html")

def clientPost(request):
  client = CLIENT()
  client.NAME = request.POST.get("nome")
  client.CPF = request.POST.get("cpf")
  client.PHONE = request.POST.get("telefone")
  client.REGISTERED = timezone.now()
  client.save()
  return HttpResponseRedirect(f"/client/get/{request.POST.get('cpf')}")

def productPost(request):
  return HttpResponseRedirect(f"/client/get/{request.POST.get('produto')}")