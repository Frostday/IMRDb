from django.db import models
from star_ratings.models import UserRating
import uuid
from django.core.validators import MaxValueValidator
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image
from io import BytesIO
from django.utils import timezone
import sys

# Create your models here.
class Movie(models.Model):
    '''
    The model to store all movies.

    Attributes:
        movie_id = In correspondance to ML model
        name = Name of movie
        stars = Rating given by user (maybe)
        image = Poster of movie
    '''
    movie_id = models.IntegerField(blank = True, null = True)
    name = models.CharField(max_length=100)
    image_url = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Movies"

    def __str__(self):
        return f"{self.name}"

class UserInputs(models.Model):
    '''
    To send the user's data to ML model

    Attributes:
        Idk under construction
    '''
    movies_selected = models.ForeignKey(Movie, on_delete=models.PROTECT, null=True, blank=True)