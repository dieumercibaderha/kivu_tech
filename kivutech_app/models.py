from django.db import models
from django.contrib.auth.models import User 


class Contact(models.Model):
    nom = models.CharField(max_length=100)
    mail = models.TextField()
    adresse = models.TextField()
    numtel = models.IntegerField()
    message = models.TextField()

class News(models.Model):
    photo = models.ImageField(upload_to='Image/', blank=True)
    description = models.TextField()

