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
  return HttpResponseRedirect("/client/get")

def productPost(request):
  # method get
  if request.method == "GET":
    return render(request, "product/post.html")

  # method post
  product = PRODUCT()
  product.NAME = request.POST.get("nome")
  product.PRICE = request.POST.get("preco")
  product.QUANTITY = request.POST.get("quantidade")
  product.REGISTERED = timezone.now()
  product.save()
  return HttpResponseRedirect("/product/get")

def clientGet(request):
  clients = CLIENT.objects.all().order_by("-REGISTERED")
  context = { "clients": clients }
  return render(request, "client/get.html", context)

def productGet(request):
  products = PRODUCT.objects.all().order_by("-REGISTERED")
  context = { "products": products }
  return render(request, "product/get.html", context)