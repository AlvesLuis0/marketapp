from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda user: user.is_superuser, "/login")
def registerEmployee(request):
	if request.method == "GET":
		return render(request, "employee/register-employee.html")
	
	try:
		user = User()
		user.username = request.POST["username"]
		user.email = request.POST["email"]
		user.set_password(request.POST["password"])

		if request.POST["role"] == "staff":
			user.is_staff = True
		
		elif request.POST["role"] == "admin":
			user.is_staff = True
			user.is_superuser = True

		user.save()
	
	except:
		messages.error(request, "Erro ao cadastrar funcionário")
		return redirect("/employee/register")
	
	messages.success(request, f"Funcionário '{user.username}' cadastrado com sucesso")
	return render(request, "employee/register-employee.html")