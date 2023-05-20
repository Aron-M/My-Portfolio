from django.db import models
from django.contrib import admin
from django.contrib.postgres.fields import ArrayField
from django.core.validators import FileExtensionValidator

# Create your models here.


class PersonalDetails(models.Model):
    full_name = models.CharField(max_length=200, unique=False)
    age = models.PositiveBigIntegerField(default='2')
    nationality = models.CharField(max_length=200, unique=False)
    residency = models.CharField(max_length=200, unique=False)
    languages = models.CharField(max_length=200, unique=False)
    studying = models.CharField(max_length=200, unique=False)
    flag_nationality = models.ImageField(upload_to='flags/', null=True, blank=True)
    flag_residency = models.ImageField(upload_to='flags/', null=True, blank=True)

    def __str__(self):
        return self.full_name


class Skills(models.Model):
    language_name = models.CharField(max_length=100)
    language_href1 = models.CharField(max_length=200)
    language_href2 = models.CharField(max_length=200)
    language_href3 = models.CharField(max_length=200)
    language_href4 = models.CharField(max_length=200)
    language_href5 = models.CharField(max_length=200)
    
    framework_name = models.CharField(max_length=100)
    framework_href1 = models.CharField(max_length=200)
    framework_href2 = models.CharField(max_length=200)
    framework_href3 = models.CharField(max_length=200)
    framework_href4 = models.CharField(max_length=200)
    framework_href5 = models.CharField(max_length=200)
    
    database_name = models.CharField(max_length=100)
    database_href1 = models.CharField(max_length=200)
    database_href2 = models.CharField(max_length=200)
    database_href3 = models.CharField(max_length=200)
    database_href4 = models.CharField(max_length=200)
    database_href5 = models.CharField(max_length=200)
    
    version_control_name = models.CharField(max_length=100)
    version_control_href1 = models.CharField(max_length=200)
    version_control_href2 = models.CharField(max_length=200)
    version_control_href3 = models.CharField(max_length=200)
    version_control_href4 = models.CharField(max_length=200)
    version_control_href5 = models.CharField(max_length=200)
    
    library_name = models.CharField(max_length=100)
    library_href1 = models.CharField(max_length=200)
    library_href2 = models.CharField(max_length=200)
    library_href3 = models.CharField(max_length=200)
    library_href4 = models.CharField(max_length=200)
    library_href5 = models.CharField(max_length=200)
    
    def __str__(self):
        return self.language_name






class Headings(models.Model):
    big_header = models.CharField(max_length=100)
    sub_header = models.CharField(max_length=100)
    par1 = models.CharField(max_length=300)
    par2 = models.CharField(max_length=300)
    par3 = models.CharField(max_length=300)
    
    def __str__(self):
        return self.big_header

class Project(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='project_images/')
    github_url = models.URLField()

    def __str__(self):
        return self.name