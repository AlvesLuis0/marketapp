from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from ..models import PERSON

def createEmployee(request):
	employee = PERSON()
	employee.CPF = request.POST.get("cpf")
	employee.USERNAME = request.POST.get("username")
	employee.PASSWORD = request.POST.get("password")
	employee.PHONE = request.POST.get("phone")
	employee.PERMISSION = "EMPLOYEE"
	employee.REGISTERED = timezone.now()
	employee.save()
	return HttpResponseRedirect(f"/?username={employee.USERNAME}&password={employee.PASSWORD}")

def employeeView(employee: PERSON):
	return HttpResponse(f"{employee.USERNAME} : {employee.PERMISSION}")