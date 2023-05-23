from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import PRODUCT

# Create your views here.
def homePage(request):
	products = PRODUCT.objects.all()
	return render(request, "index.html", {
		"products": products
	})

def loginPage(request):
	if request.method == "GET":
		return render(request, "login.html")
	
	user = authenticate(request,
		username=request.POST["username"],
		password=request.POST["password"]
	)

	if user is not None:
		login(request, user)
		return redirect("/")

	return render(request, "login.html", { "error": True })

def signoutPage(request):
	logout(request)
	return redirect("/")