# Generated by Django 3.2.18 on 2023-05-24 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_pf', '0003_auto_20230524_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldetails',
            name='study_icon',
            field=models.ImageField(blank=True, null=True, upload_to='study-icon/'),
        ),
    ]
