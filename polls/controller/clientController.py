from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from ..models import PERSON

def createClient(request):
	client = PERSON()
	client.CPF = request.POST.get("cpf")
	client.USERNAME = request.POST.get("username")
	client.PASSWORD = request.POST.get("password")
	client.PHONE = request.POST.get("phone")
	client.PERMISSION = "CLIENT"
	client.REGISTERED = timezone.now()
	client.save()
	return HttpResponseRedirect(f"/?username={client.USERNAME}&password={client.PASSWORD}")

def clientView(request):
	try:
		client = PERSON.objects.get(
			USERNAME=request.GET.get("username"),
			PASSWORD=request.GET.get("password")
		)
		return  HttpResponse(client.USERNAME)

	except:
		return HttpResponseRedirect("/register")
	