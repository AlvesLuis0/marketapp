from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ..models import PRODUCT

def getProducts(request):
	products = PRODUCT.objects.all()
	return render(request, "product/products.html", {
		"products": products
	})

@login_required(login_url="/login/")
def registerProduct(request):
	if request.method == "GET":
		return render(request, "product/register.html")
	
	product = PRODUCT()
	product.NAME = request.POST["name"]
	product.PRICE = request.POST["price"]
	product.QUANTITY = request.POST["quantity"]
	product.save()
	
	messages.success(request, f"Produto '{product.NAME}' cadastrado com sucesso")
	return render(request, "auth/login.html")