# Generated by Django 4.2.4 on 2023-09-08 17:54

import apps.ufc_base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ufc_base', '0003_alter_fighterprofile_number_of_fights'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fighterprofile',
            name='c_photo',
            field=models.ImageField(upload_to=apps.ufc_base.models.c_photo),
        ),
        migrations.AlterField(
            model_name='fighterprofile',
            name='f_photo',
            field=models.ImageField(upload_to=apps.ufc_base.models.f_photo),
        ),
    ]
