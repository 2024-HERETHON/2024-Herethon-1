# Generated by Django 5.0.6 on 2024-06-29 12:22

import mainApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, upload_to=mainApp.models.upload_filepath),
        ),
    ]