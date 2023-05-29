from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ..models import PRODUCT

def getAllProducts(request):
	products = PRODUCT.objects.all()
	return render(request, "product/all-products.html", {
		"products": products
	})

@login_required(login_url="/login/")
def updateProduct(request, pk):
	try:
		product = PRODUCT.objects.get(pk=pk)
		product.NAME = request.POST["name"]
		product.PRICE = request.POST["price"]
		product.QUANTITY = request.POST["quantity"]
		product.save()
		messages.success(request, f"'{product.NAME}' atualizado com sucesso!")
	
	except:
		messages.error(request, "Erro ao atualizar produto")
	
	return redirect(f"/product/{pk}")

def getProduct(request, pk):
	template = "product/product-detail.html"

	if request.user.is_staff:
		template = "product/update-product.html"
	
	return render(request, template, {
		"product": PRODUCT.objects.get(pk=pk)
	})

@login_required(login_url="/login/")
def deleteProduct(request, pk):
	try:
		PRODUCT.objects.get(pk=pk).delete()
	
	except: pass

	return redirect("/")

@login_required(login_url="/login/")
def registerProduct(request):
	if request.method == "GET":
		return render(request, "product/register-product.html")
	
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
	return render(request, "product/register-product.html")