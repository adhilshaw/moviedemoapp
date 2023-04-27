from django.db import models


# Create your models here.
class Movie(models.Model):
    id = models.BigAutoField(
        primary_key=True
    )
    name = models.CharField(
        max_length=250,
        verbose_name="Moive name"
    )
    desc = models.TextField(
        verbose_name="Description"
    )
    year = models.PositiveBigIntegerField(
        verbose_name="release year"
    )
    image = models.ImageField(
        upload_to='gallery',
        verbose_name="Images"
    )
    director = models.CharField(
        max_length=100
    )
    

