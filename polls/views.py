from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone

from .models import CLIENT, PRODUCT

# Create your views here.
def index(request):
  return render(request, "index.html")

def clientPost(request):
  # method get
  if request.method == "GET":
    return render(request, "client/post.html")

  # method post
  client = CLIENT()
  client.NAME = request.POST.get("nome")
  client.CPF = request.POST.get("cpf")
  client.PHONE = request.POST.get("telefone")
  client.REGISTERED = timezone.now()
  client.save()
  return HttpResponseRedirect(f"/client/get/{request.POST.get('cpf')}")

def productPost(request):
  # method get
  if request.method == "GET":
    return render(request, "product/post.html")

  # method post
  product = PRODUCT()
  product.NAME = request.POST.get("produto")
  product.PRICE = request.POST.get("valor")
  product.QUANTITY = request.POST.get("quantidade")
  product.REGISTERED = timezone.now()
  product.save()
  return HttpResponseRedirect(f"/client/get/{product.ID}")