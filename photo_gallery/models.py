from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.forms.models import modelform_factory

# Create your models here.

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class ImageModel(models.Model):
	image = models.ImageField(upload_to=user_directory_path)
	creation_date = models.DateField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	#def save(self, *args, **kwargs):
    #    do_something()
    #    super(ImageModel, self).save(*args, **kwargs) # Call the "real" save() method.
    #    do_something_else()
	
ImageUploadForm = modelform_factory(ImageModel, fields=('image',))