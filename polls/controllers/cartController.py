from django.shortcuts import redirect
from django.contrib import messages
from ..models import PRODUCT

def addToCart(request, pk):
    product = PRODUCT.objects.get(pk=pk)

    if product:
        cart = request.session.get("cart")

        if not cart:
            cart = []

        for i in cart:
            if i[0] == product.id:
                i[1] = request.POST.get("quantity")

        cart.append((product.id, request.POST.get("quantity")))
        request.session["cart"] = cart
        messages.success(request, f"'{product.NAME}' adicionado ao carrinho")
        return redirect("/")
    
    messages.error("Erro ao adicionar produto ao carrinho")
    return redirect("/")