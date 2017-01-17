from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from photo_gallery.models import ImageModel, ImageUploadForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def mystub(request):
	return HttpResponse("Hello world")
	
def home(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect(reverse('profile', kwargs={'id': request.user.id}))
	else:
		return HttpResponseRedirect(reverse('login'))
	
def registration(request):
	if request.method =='POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			return HttpResponseRedirect(reverse('registered'))
	else:
		form = UserCreationForm()
	return render(request, 'registration/registration.html', {'form': form})
	
@login_required
def registered(request):
	return render(request, 'registration/registered.html')
	
@login_required
def profile(request, id=0):
	if id==0:
		curruser = request.user
	else:
		curruser = User.objects.get(pk=id)
	user = request.user
	userlist = User.objects.exclude(id=user.id).exclude(id=curruser.id)
	return render(request, 'registration/profile.html', {'user':user, 'curruser':curruser, 'userlist':userlist})

@login_required
def upload_image(request):
	if request.method == 'POST' :
		form = ImageUploadForm(request.POST, request.FILES)
		if form.is_valid():
			image = form.save(commit=False)
			image.user = User.objects.get(pk=int(request.user.id))
			image.save()
			return HttpResponseRedirect(reverse('home'))
		else:
			return HttpResponse("Picture is not valid")
	else:
		form = ImageUploadForm()
	return render(request, 'registration/upload_image.html', {'form': form})
	
@login_required
def fullsize_image(request, imageid):
	image_url = ImageModel.objects.get(pk=imageid).image.url
	return render(request, 'registration/fullsize_image.html', {'image_url': image_url})
	