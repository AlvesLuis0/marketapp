from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpRequest

def loginController(request: HttpRequest):
	if request.method == "GET":
		return render(request, "auth/login.html")
	
	user = authenticate(request,
		username=request.POST["username"],
		password=request.POST["password"]
	)

	if user is not None:
		login(request, user)
		return redirect("/")

	messages.error(request, "Usuário ou senha incorretos")
	return redirect("/login")

def logoutController(request):
	logout(request)
	return redirect("/")