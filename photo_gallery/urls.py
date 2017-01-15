from django.conf.urls import url, include

import photo_gallery.views

urlpatterns = [
	url(r'^register_user/', photo_gallery.views.register_user, name='register_user'),
	url(r'^', include('django.contrib.auth.urls'), {'template_name': 'registration/login.html'}),
]
