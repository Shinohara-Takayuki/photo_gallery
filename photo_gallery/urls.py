from django.conf.urls import url, include

import photo_gallery.views
import django.contrib.auth.views

urlpatterns = [
	url(r'^registration/', photo_gallery.views.registration, name='registration'),
	url(r'^register_user/', photo_gallery.views.register_user, name='register_user'),
	url(r'^registered/', photo_gallery.views.registered, name='registered'),
	url(r'^login/$', django.contrib.auth.views.login, {'template_name': 'registration/login.html'}, name='login'),
	url(r'^profile/', photo_gallery.views.profile, name='profile'),
]
