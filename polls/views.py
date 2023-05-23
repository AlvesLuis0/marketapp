from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import PRODUCT

# Create your views here.
def home(request):
	products = PRODUCT.objects.all()
	return render(request, "index.html", {
		"products": products
	})

def login(request):
	if request.method == "GET":
		return render(request, "login.html")
	
	get_object_or_404(User,
		username=request.POST["username"],
		password=request.POST["password"]
	)
	
	print("logado")
	return render(request)