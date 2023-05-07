from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import FileExtensionValidator

# Create your models here.


class PersonalDetails(models.Model):
    full_name = models.CharField(max_length=200, unique=False)
    age = models.PositiveBigIntegerField
    nationality = models.CharField(max_length=200, unique=False)
    residency = models.CharField(max_length=200, unique=False)
    languages = models.CharField(max_length=200, unique=False)
    address = models.CharField(max_length=200, unique=False)

    def __str__(self):
            return self.full_name


class Skills(models.Model):
    languages = models.CharField(max_length=200, unique=False)
    frameworks = models.CharField(max_length=200, unique=False)
    version_control = models.CharField(max_length=200, unique=False)
    databases = models.CharField(max_length=200, unique=False)

    def __str__(self):
            return self.languages


class Language(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='languages/', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])

    def __str__(self):
        return self.name


class Framework(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='frameworks/', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])

    def __str__(self):
        return self.name


    
    