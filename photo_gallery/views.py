from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# Create your views here.

def mystub(request):
	return HttpResponse("Hello world")
	
def registration(request):
	return render(request, 'registration/registration.html')
	
def register_user(request):
	user = User.objects.create_user(request.POST['username'], 
									request.POST['email'], 
									request.POST['password'])
	user.last_name = request.POST['lastname']
	user.first_name = request.POST['firstname']
	user.save()
	return HttpResponseRedirect(reverse('registered'))
	
def registered(request):
	return render(request, 'registration/registered.html')
	