from django.db import models

# Create your models here.
class PersonalDetails(models.Model):
    full_name = CharField
    age = PositiveBigInteger
    nationality = CharField
    residency = CharField
    languages = CharField
    address = CharField


    