from django.conf.urls import url, include

import photo_gallery.views
import django.contrib.auth.views

urlpatterns = [
	url(r'^registration/', photo_gallery.views.registration, name='registration'),
	url(r'^registered/', photo_gallery.views.registered, name='registered'),
	url(r'^login/$', django.contrib.auth.views.login, {'template_name': 'registration/login.html'}, name='login'),
	url(r'^profile/', photo_gallery.views.profile, name='profile'),
	url(r'^logout/$', django.contrib.auth.views.logout, {'next_page': 'login'}, name='logout'),
	url(r'^upload_image/', photo_gallery.views.upload_image, name='upload_image'),
]
