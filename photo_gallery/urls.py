from django.conf.urls import url, include

import photo_gallery.views

urlpatterns = [
	url(r'^registration/', photo_gallery.views.registration, name='registration'),
	url(r'^register_user/', photo_gallery.views.register_user, name='register_user'),
	url(r'^registered/', photo_gallery.views.registered, name='registered'),
	url(r'^', include('django.contrib.auth.urls'), {'template_name': 'registration/login.html'}),
]
