from __future__ import unicode_literals
from PIL import Image
import StringIO
from django.db import models
from django.contrib.auth.models import User
from django.forms.models import modelform_factory
from django.core.files.base import ContentFile 
from guardian.shortcuts import assign_perm


# Create your models here.

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class ImageModel(models.Model):
	image = models.ImageField(upload_to=user_directory_path)
	icon = models.ImageField(upload_to=user_directory_path, blank=True)
	upload_date = models.DateField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	
	def make_icon(self):	
		snapshot = Image.open(self.image)
		(width, height) = snapshot.size
		size = (200, 200 * height / width)
		
		thumb = snapshot.resize(size)
		thumb_io = StringIO.StringIO()
		thumb.save(thumb_io, format='PNG')
		
		self.icon.save("%s-small.png" %self.image.name.split('.')[0], ContentFile(thumb_io.getvalue()), save=True)
	
	def save(self, *args, **kwargs):
		super(ImageModel, self).save(*args, **kwargs)
		assign_perm('view_image', self.user, self)
		if not self.icon:
			self.make_icon()
			
	class Meta:
		permissions = (
		("view_image", "View image"),
		)

class PermRequest(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ForeignKey(ImageModel, on_delete=models.CASCADE)
	perm = models.CharField(max_length = 100)
		
ImageUploadForm = modelform_factory(ImageModel, fields=('image',))