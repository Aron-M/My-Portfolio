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
    image1 = models.ImageField(
        upload_to='skills/', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    image2 = models.ImageField(
        upload_to='skills/', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    image3 = models.ImageField(
        upload_to='skills/', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    image4 = models.ImageField(
        upload_to='skills/', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    image5 = models.ImageField(
        upload_to='skills/', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])

    def __str__(self):
        return self.name


class Framework(models.Model):
    name = models.CharField(max_length=100)
    image1 = models.ImageField(
        upload_to='skills/', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    image2 = models.ImageField(
        upload_to='skills/', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    image3 = models.ImageField(
        upload_to='skills/', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    image4 = models.ImageField(
        upload_to='skills/', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    image5 = models.ImageField(
        upload_to='skills/', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])

    def __str__(self):
        return self.name


class Library(models.Model):
    name = models.CharField(max_length=100)
    image1 = models.ImageField(
        upload_to='libraries/', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    image2 = models.ImageField(
        upload_to='libraries/', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    image3 = models.ImageField(
        upload_to='libraries/', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])

    def __str__(self):
        return self.name

class VersionControl(models.Model):
    name = models.CharField(max_length=100)
    image1 = models.ImageField(
        upload_to='version-control/', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    image2 = models.ImageField(
        upload_to='version-control/', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    image3 = models.ImageField(
        upload_to='version-control/', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])

    def __str__(self):
        return self.name