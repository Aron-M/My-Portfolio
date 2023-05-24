from django.db import models
from django.contrib import admin
from django.contrib.postgres.fields import ArrayField
from django.core.validators import FileExtensionValidator

# Create your models here.


class PersonalDetails(models.Model):
    full_name = models.CharField(max_length=200, unique=False)
    nationality = models.CharField(max_length=200, unique=False)
    residency = models.CharField(max_length=200, unique=False)
    languages = models.CharField(max_length=200, unique=False)
    studying = models.CharField(max_length=200, unique=False)
    flag_nationality = models.ImageField(upload_to='flags/', null=True, blank=True)
    flag_residency = models.ImageField(upload_to='flags/', null=True, blank=True)

    def __str__(self):
        return self.full_name


class Skills(models.Model):
    language_heading = models.CharField(max_length=100)
    language_icon1 = models.URLField(max_length=100, blank=True, null=True)
    language_name1 = models.CharField(max_length=100, blank=True, null=True)
    language_icon2 = models.URLField(max_length=100, blank=True, null=True)
    language_name2 = models.CharField(max_length=100, blank=True, null=True)
    language_icon3 = models.URLField(max_length=100, blank=True, null=True)
    language_name3 = models.CharField(max_length=100, blank=True, null=True)
    language_icon4 = models.URLField(max_length=100, blank=True, null=True)
    language_name4 = models.CharField(max_length=100, blank=True, null=True)
    language_icon5 = models.URLField(max_length=100, blank=True, null=True)
    language_name5 = models.CharField(max_length=100, blank=True, null=True)

    framework_heading = models.CharField(max_length=100)
    framework_icon1 = models.URLField(max_length=100, blank=True, null=True)
    framework_name1 = models.CharField(max_length=100, blank=True, null=True)
    framework_icon2 = models.URLField(max_length=100, blank=True, null=True)
    framework_name2 = models.CharField(max_length=100, blank=True, null=True)
    framework_icon3 = models.URLField(max_length=100, blank=True, null=True)
    framework_name3 = models.CharField(max_length=100, blank=True, null=True)
    framework_icon4 = models.URLField(max_length=100, blank=True, null=True)
    framework_name4 = models.CharField(max_length=100, blank=True, null=True)
    framework_icon5 = models.URLField(max_length=100, blank=True, null=True)
    framework_name5 = models.CharField(max_length=100, blank=True, null=True)
    
    database_heading = models.CharField(max_length=100)
    database_icon1 = models.URLField(max_length=100, blank=True, null=True)
    database_name1= models.CharField(max_length=100, blank=True, null=True)
    database_icon2 = models.URLField(max_length=100, blank=True, null=True)
    database_name2= models.CharField(max_length=100, blank=True, null=True)
    database_icon3 = models.URLField(max_length=100, blank=True, null=True)
    database_name3= models.CharField(max_length=100, blank=True, null=True)
    database_icon4 = models.URLField(max_length=100, blank=True, null=True)
    database_name4= models.CharField(max_length=100, blank=True, null=True)
    database_icon5 = models.URLField(max_length=100, blank=True, null=True)
    database_name5= models.CharField(max_length=100, blank=True, null=True)
    
    version_control_heading = models.CharField(max_length=100)
    version_control_icon1 = models.URLField(max_length=100, blank=True, null=True)
    version_control_name1 = models.CharField(max_length=100, blank=True, null=True)
    version_control_icon2 = models.URLField(max_length=100, blank=True, null=True)
    version_control_name2 = models.CharField(max_length=100, blank=True, null=True)
    version_control_icon3 = models.URLField(max_length=100, blank=True, null=True)
    version_control_name3 = models.CharField(max_length=100, blank=True, null=True)
    version_control_icon4 = models.URLField(max_length=100, blank=True, null=True)
    version_control_name4 = models.CharField(max_length=100, blank=True, null=True)
    version_control_icon5 = models.URLField(max_length=100, blank=True, null=True)
    version_control_name5 = models.CharField(max_length=100, blank=True, null=True)
    
    library_heading = models.CharField(max_length=100)
    library_icon1 = models.URLField(max_length=100, blank=True, null=True)
    library_name1 = models.CharField(max_length=100, blank=True, null=True)
    library_icon2 = models.URLField(max_length=100, blank=True, null=True)
    library_name2 = models.CharField(max_length=100, blank=True, null=True)
    library_icon3 = models.URLField(max_length=100, blank=True, null=True)
    library_name3 = models.CharField(max_length=100, blank=True, null=True)
    library_icon4 = models.URLField(max_length=100, blank=True, null=True)
    library_name4 = models.CharField(max_length=100, blank=True, null=True)
    library_icon5 = models.URLField(max_length=100, blank=True, null=True)
    library_name5 = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.language_name1




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
    description = models.CharField(max_length=200)
    github_url = models.URLField()

    def __str__(self):
        return self.name