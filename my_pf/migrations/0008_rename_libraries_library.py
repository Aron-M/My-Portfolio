# Generated by Django 3.2.18 on 2023-05-08 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_pf', '0007_libraries'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Libraries',
            new_name='Library',
        ),
    ]