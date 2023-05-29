from django.db import models
from django.contrib.auth.models import user
from cloudinary.models import CloudinaryField

from djrichtextfeld.models import RichTextField

# Create your models here.

Class Holidays(models.Model):

    user = models.Foreignkey(User, related_name='receipe owner,' on_delete=models.CASCADE)
    title = models.Charfield(max_length=300, null =False, blank=False)
    description = models.Charfield(max_length=500, null=False, blank=False)
    Instructions = RichTextField (max_length=10000, null=False, blank=False)
    Highlights = RichTextField(max_length=10000, null=False, blank=False)
    image = ResizedImageField(
        size={400, None}, quality=75, upload_to='recipes/', force_format='WEBP'
        blank=False, null=False 
    ) 

    def_str_(self):
        return self.title

