from django.db import models
import uuid
from django.core.validators import MaxValueValidator

# Create your models here.
class Movie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    stars = models.SmallIntegerField(default = 0, validators=[MaxValueValidator(5)])

    class Meta:
        verbose_name_plural = "Movies"

    def __str__(self):
        return f"{self.name}"