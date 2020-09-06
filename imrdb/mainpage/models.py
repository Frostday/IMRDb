from django.db import models
import uuid
from django.core.validators import MaxValueValidator
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image
from io import BytesIO
import sys

# Create your models here.
class Movie(models.Model):
    movie_id = models.IntegerField(blank = True, null = True)
    name = models.CharField(max_length=100)
    stars = models.SmallIntegerField(default = 0, validators=[MaxValueValidator(5)])
    image = models.ImageField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Movies"

    def compressImage(self, image):
        imageTemproary = Image.open(image)
        outputIoStream = BytesIO()
        # imageTemproaryResized = imageTemproary.resize((1020, 573))
        imageTemproary.save(outputIoStream, format='JPEG', quality=60)
        outputIoStream.seek(0)
        image = InMemoryUploadedFile(outputIoStream, 'ImageField', "%s.jpg" % image.name.split('.')[
            0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        return image

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def __str__(self):
        return f"{self.name}"