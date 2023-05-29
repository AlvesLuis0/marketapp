from django.shortcuts import render, redirect
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
	
	try:
		product = PRODUCT()
		product.NAME = request.POST["name"]
		product.PRICE = request.POST["price"]
		product.QUANTITY = request.POST["quantity"]
		product.save()
	
	except:
		messages.error(request, "Erro ao cadastrar produto")
		return redirect("/product/register")
	
	messages.success(request, f"Produto '{product.NAME}' cadastrado com sucesso")
	return render(request, "product/register.html")