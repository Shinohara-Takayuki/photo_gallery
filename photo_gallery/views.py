from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def register_user(request):
	return render(request, 'registration/register_user.html')
	
def mystub(request):
	return HttpResponse("Hello world")