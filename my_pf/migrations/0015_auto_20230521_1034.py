# Generated by Django 3.2.18 on 2023-05-21 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_pf', '0014_auto_20230520_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='skills',
            name='language_name1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='skills',
            name='language_name2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='skills',
            name='language_name3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='skills',
            name='language_name4',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='skills',
            name='language_name5',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
