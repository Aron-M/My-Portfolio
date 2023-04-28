from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PersonalDetails(models.Model):
    full_name = models.CharField(max_length=200, unique=False)
    age = models.PositiveBigIntegerField
    nationality = models.CharField(max_length=200, unique=False)
    residency = models.CharField(max_length=200, unique=False)
    languages = models.CharField(max_length=200, unique=False)
    address = models.CharField(max_length=200, unique=False)

    class Meta:

        def __str__(self):
            return self.title

    
    