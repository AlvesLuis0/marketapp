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

@user_passes_test(lambda user: user.is_superuser, "/login")
def getAllEmployees(request):
	employees = User.objects.all()
	return render(request, "employee/all-employees.html", {
		"employees": employees
	})

@user_passes_test(lambda user: user.is_superuser, "/login")
def getEmployee(request, pk):
	return render(request, "employee/update-employee.html", {
		"employee": User.objects.get(pk=pk)
	})

@user_passes_test(lambda user: user.is_superuser, "/login")
def updateEmployee(request, pk):
	try:
		user = User.objects.get(pk=pk)
		user.username = request.POST["username"]
		user.email = request.POST["email"]
		user.set_password(request.POST["password"])

		if request.POST["role"] == "staff":
			user.is_staff = True
		
		elif request.POST["role"] == "admin":
			user.is_staff = True
			user.is_superuser = True

		user.save()
		messages.success(request, f"'{user.username}' atualizado com sucesso!")
	
	except:
		messages.error(request, "Erro ao atualizar funcionário")
	
	return redirect(f"/employee/{pk}")

@user_passes_test(lambda user: user.is_superuser, "/login")
def deleteEmployee(request, pk):
	try:
		User.objects.get(pk=pk).delete()
	
	except: pass

	return redirect("/employee")