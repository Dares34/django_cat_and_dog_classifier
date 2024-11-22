from django.db import models
from django.urls import reverse
from django.conf import settings
import os

class PetClassifier(models.Model):

    image = models.ImageField(upload_to='pet_images/')
    label = models.CharField(max_length=10)

    def save(self, *args, **kwargs):
        directory = os.path.join(settings.MEDIA_ROOT, 'pet_images/')

        if not os.path.exists(directory):
            os.makedirs(directory)

        super(PetClassifier, self).save(*args, **kwargs)