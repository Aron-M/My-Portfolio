# Generated by Django 3.2.18 on 2023-05-06 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_pf', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('languages', models.CharField(max_length=200)),
                ('frameworks', models.CharField(max_length=200)),
                ('version_control', models.CharField(max_length=200)),
                ('databases', models.CharField(max_length=200)),
            ],
        ),
    ]