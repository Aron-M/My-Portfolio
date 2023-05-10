# Generated by Django 3.2.18 on 2023-05-10 18:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_pf', '0010_auto_20230509_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='versioncontrol',
            name='image1',
            field=models.ImageField(upload_to='database/', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])]),
        ),
        migrations.AlterField(
            model_name='versioncontrol',
            name='image2',
            field=models.ImageField(upload_to='database/', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])]),
        ),
        migrations.AlterField(
            model_name='versioncontrol',
            name='image3',
            field=models.ImageField(upload_to='database/', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])]),
        ),
        migrations.AlterField(
            model_name='versioncontrol',
            name='image4',
            field=models.ImageField(upload_to='database/', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])]),
        ),
        migrations.AlterField(
            model_name='versioncontrol',
            name='image5',
            field=models.ImageField(upload_to='database/', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])]),
        ),
    ]
