from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def mystub(request):
	return HttpResponse("Hello world")
	
def registration(request):
	if request.method =='POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			return HttpResponseRedirect(reverse('registered'))
	else:
		form = UserCreationForm()
	return render(request, 'registration/registration.html', {'form': form})
	
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
	
def profile(request):
	return HttpResponse('Profile page')
	