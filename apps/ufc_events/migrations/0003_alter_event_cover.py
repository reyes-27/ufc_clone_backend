# Generated by Django 4.2.4 on 2023-10-27 16:32

import apps.ufc_events.models
from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('ufc_events', '0002_event_cover_event_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='cover',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='PNG', keep_meta=True, null=True, quality=100, scale=1, size=[1920, 1080], upload_to=apps.ufc_events.models.event_cover),
        ),
    ]