from django.db import models
from django.contrib import admin
from django.contrib.postgres.fields import ArrayField
from django.core.validators import FileExtensionValidator


class PersonalDetails(models.Model):
    full_name = models.CharField(max_length=200, unique=False)
    nationality = models.CharField(max_length=200, unique=False)
    residency = models.CharField(max_length=200, unique=False)
    languages = models.CharField(max_length=200, unique=False)
    studying = models.CharField(max_length=200, unique=False)
    flag_nationality = models.ImageField(upload_to='flags/', null=True, blank=True)
    flag_residency = models.ImageField(upload_to='flags/', null=True, blank=True)
    study_icon = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.full_name

class Headings(models.Model):
    big_header = models.CharField(max_length=100)
    sub_header = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='images/', null=True, blank=True)
    par1 = models.CharField(max_length=300)
    par2 = models.CharField(max_length=300)
    par3 = models.CharField(max_length=300)
    par4 = models.CharField(max_length=300)
    
    def __str__(self):
        return self.big_header

class Project(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/project_images/', null=True, blank=True)
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

