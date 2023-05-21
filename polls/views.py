from django.shortcuts import render
from django.http import HttpResponseRedirect
from .controller import clientController, employeeController
from .models import PERSON

# Create your views here.
def login(request):
	return render(request, "login.html")

def register(request):
	return render(request, "register.html")

def panel(request):
	try:
		person = PERSON.objects.get(
			USERNAME=request.GET.get("username"),
			PASSWORD=request.GET.get("password")
		)
	
		if person.PERMISSION == "CLIENT":
			return clientController.clientView(person)

		if person.PERMISSION == "EMPLOYEE":
			return employeeController.employeeView(person)

	except:
		return HttpResponseRedirect("/register")

createClient = clientController.createClient
clientView = clientController.clientView