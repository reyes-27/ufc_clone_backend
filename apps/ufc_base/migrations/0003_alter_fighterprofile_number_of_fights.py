# Generated by Django 4.2.4 on 2023-09-08 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ufc_base', '0002_fighterprofile_fighter_slug_alter_fighterprofile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fighterprofile',
            name='number_of_fights',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]