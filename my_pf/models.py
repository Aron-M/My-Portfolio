from django.db import models
from django.contrib import admin
from django.contrib.postgres.fields import ArrayField
from django.core.validators import FileExtensionValidator
from cloudinary_storage.models import CloudinaryField


class PersonalDetails(models.Model):
    full_name = models.CharField(max_length=200, unique=False)
    nationality = models.CharField(max_length=200, unique=False)
    residency = models.CharField(max_length=200, unique=False)
    languages = models.CharField(max_length=200, unique=False)
    studying = models.CharField(max_length=200, unique=False)
    flag_nationality = models.ImageField(upload_to='media', null=True, blank=True)
    flag_residency = models.ImageField(upload_to='media', null=True, blank=True)
    study_icon = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.full_name

class Headings(models.Model):
    big_header = models.CharField(max_length=100, null=True, blank=True)
    sub_header = models.CharField(max_length=100, null=True, blank=True)
    profile_image = models.CloudinaryField(upload_to='media', null=True, blank=True)
    par1 = models.CharField(max_length=300, null=True, blank=True)
    par2 = models.CharField(max_length=300, null=True, blank=True)
    
    def __str__(self):
        return self.big_header


class Project(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media', null=True, blank=True)
    description = models.CharField(max_length=200)
    github_url = models.URLField()

    def __str__(self):
        return self.name



class SkillCategory(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Skills(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    icon = models.URLField(max_length=100, blank=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    progress = models.ImageField(upload_to='progress/', null=True, blank=True)
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

