from django.shortcuts import render
from ..models import PRODUCT

def getProducts(request):
	products = PRODUCT.objects.all()
	return render(request, "index.html", {
		"products": products
	})