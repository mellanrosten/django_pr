# Generated by Django 3.0.5 on 2020-04-19 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publication',
            old_name='datetime',
            new_name='date',
        ),
    ]
