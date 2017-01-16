from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from photo_gallery.models import ImageModel, ImageUploadForm

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
	
def registered(request):
	return render(request, 'registration/registered.html')
	
def profile(request):
	user = request.user
	return render(request, 'registration/profile.html')

def upload_image(request):
	if request.method == 'POST' :
		form = ImageUploadForm(request.POST, request.FILES)
		if form.is_valid():
			image = form.save(commit=False)
			image.user = User.objects.get(pk=int(request.user.id))
			image.save()
			return HttpResponseRedirect(reverse('profile'))
		else:
			return HttpResponse("Picture is not valid")
	else:
		form = ImageUploadForm()
	return render(request, 'registration/upload_image.html', {'form': form})
	