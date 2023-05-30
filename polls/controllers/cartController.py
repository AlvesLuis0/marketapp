from django.shortcuts import redirect
from django.contrib import messages
from ..models import PRODUCT

def findProduct(cart, pk):
	for i in range(len(cart)):
		if cart[i][0] == pk: return i
	
	return -1

def addToCart(request, pk):
	product = PRODUCT.objects.get(pk=pk)

	if product:
		cart = request.session.get("cart")

		if not cart:
			cart = []

		print(cart)
		index = findProduct(cart, pk)
		quantity = request.POST.get("quantity")

		if index == -1:
			cart.append([product.id, quantity])
		
		else:
			cart[index] = [product.id, quantity]

		request.session["cart"] = cart
		print(cart)
		messages.success(request, f"'{product.NAME}' x{quantity} adicionado ao carrinho")
		return redirect("/")
	
	messages.error("Erro ao adicionar produto ao carrinho")
	return redirect("/")