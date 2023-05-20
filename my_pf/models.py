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
    language_icon1 = models.URLField(max_length=100, blank=True, null=True)
    language_icon2 = models.URLField(max_length=100, blank=True, null=True)
    language_icon3 = models.URLField(max_length=100, blank=True, null=True)
    language_icon4 = models.URLField(max_length=100, blank=True, null=True)
    language_icon5 = models.URLField(max_length=100, blank=True, null=True)
    
    framework_name = models.CharField(max_length=100)
    framework_icon1 = models.URLField(max_length=100, blank=True, null=True)
    framework_icon2 = models.URLField(max_length=100, blank=True, null=True)
    framework_icon3 = models.URLField(max_length=100, blank=True, null=True)
    framework_icon4 = models.URLField(max_length=100, blank=True, null=True)
    framework_icon5 = models.URLField(max_length=100, blank=True, null=True)
    
    database_name = models.CharField(max_length=100)
    database_icon1 = models.URLField(max_length=100, blank=True, null=True)
    database_icon2 = models.URLField(max_length=100, blank=True, null=True)
    database_icon3 = models.URLField(max_length=100, blank=True, null=True)
    database_icon4 = models.URLField(max_length=100, blank=True, null=True)
    database_icon5 = models.URLField(max_length=100, blank=True, null=True)
    
    version_control_name = models.CharField(max_length=100)
    version_control_icon1 = models.URLField(max_length=100, blank=True, null=True)
    version_control_icon2 = models.URLField(max_length=100, blank=True, null=True)
    version_control_icon3 = models.URLField(max_length=100, blank=True, null=True)
    version_control_icon4 = models.URLField(max_length=100, blank=True, null=True)
    version_control_icon5 = models.URLField(max_length=100, blank=True, null=True)
    
    library_name = models.CharField(max_length=100)
    library_icon1 = models.URLField(max_length=100, blank=True, null=True)
    library_icon2 = models.URLField(max_length=100, blank=True, null=True)
    library_icon3 = models.URLField(max_length=100, blank=True, null=True)
    library_icon4 = models.URLField(max_length=100, blank=True, null=True)
    library_icon5 = models.URLField(max_length=100, blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if self.language_name:
            self.language_icon1 = get_devicon(self.language_name)
            self.language_icon2 = get_devicon(self.language_name)
            self.language_icon3 = get_devicon(self.language_name)
            self.language_icon4 = get_devicon(self.language_name)
            self.language_icon5 = get_devicon(self.language_name)
        if self.framework_name:
            self.framework_icon1 = get_devicon(self.framework_name)
            self.framework_icon2 = get_devicon(self.framework_name)
            self.framework_icon3 = get_devicon(self.framework_name)
            self.framework_icon4 = get_devicon(self.framework_name)
            self.framework_icon5 = get_devicon(self.framework_name)
        if self.database_name:
            self.database_icon1 = get_devicon(self.database_name)
            self.database_icon2 = get_devicon(self.database_name)
            self.database_icon3 = get_devicon(self.database_name)
            self.database_icon4 = get_devicon(self.database_name)
            self.database_icon5 = get_devicon(self.database_name)
        if self.version_control_name:
            self.version_control_icon1 = get_devicon(self.version_control_name)
            self.version_control_icon2 = get_devicon(self.version_control_name)
            self.version_control_icon3 = get_devicon(self.version_control_name)
            self.version_control_icon4 = get_devicon(self.version_control_name)
            self.version_control_icon5 = get_devicon(self.version_control_name)
        if self.library_name:
            self.library_icon1 = get_devicon(self.library_name)
            self.library_icon2 = get_devicon(self.library_name)
            self.library_icon3 = get_devicon(self.library_name)
            self.library_icon4 = get_devicon(self.library_name)
            self.library_icon5 = get_devicon(self.library_name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.language_name

def get_devicon(name):
    # Implement your logic to retrieve the icon URL from www.devicon.dev based on the name
    # You can use web scraping, an API, or any other method to fetch the icon URL.
    # Return the icon URL as a string.
    # Example implementation:
    # return f"https://www.devicon.dev/icons/{name}/{name}-original.svg"

    # Placeholder implementation returning None
    return (
          
           "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original-wordmark.svg"
          
          )






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