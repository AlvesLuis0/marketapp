from django.shortcuts import redirect, render
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from ..models import PRODUCT

def findProduct(cart, pk):
	for i in range(len(cart)):
		if cart[i][0] == pk: return i
	
	return -1

@user_passes_test(lambda user: not user.is_staff, "/")
def addToCart(request, pk):
	product = PRODUCT.objects.get(pk=pk)

	if product:
		cart = request.session.get("cart")

		if not cart:
			cart = []

		index = findProduct(cart, pk)
		quantity = request.POST.get("quantity")

		if index == -1:
			cart.append([product.id, quantity])
		
		else:
			cart[index] = [product.id, quantity]

		request.session["cart"] = cart
		messages.success(request, f"'{product.NAME}' x{quantity} adicionado ao carrinho")
		return redirect("/")
	
	messages.error("Erro ao adicionar produto ao carrinho")
	return redirect("/")

@user_passes_test(lambda user: not user.is_staff, "/")
def getCart(request):
	cart = request.session.get("cart")
	products = []

	if not cart:
		cart = []
	
	for i in cart:
		product = PRODUCT.objects.get(pk=i[0])
		products.append({
			"NAME": product.NAME,
			"PRICE": product.PRICE,
			"QUANTITY": i[1],
			"id": product.id
		})

	return render(request, "product/cart.html", { "products": products })

@user_passes_test(lambda user: not user.is_staff, "/")
def deleteFromCart(request, pk):
	cart = request.session.get("cart")

	if not cart:
		cart = []
	
	index = findProduct(cart, pk)

	if index == -1:
		messages.error("Não foi possível remover este item")
		return redirect("/product/cart")
	
	cart.remove(cart[index])
	request.session["cart"] = cart
	return redirect("/product/cart/")