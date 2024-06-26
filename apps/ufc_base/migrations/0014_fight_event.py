# Generated by Django 4.2.6 on 2024-06-02 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ufc_events', '0004_remove_event_bout'),
        ('ufc_base', '0013_alter_fighterprofile_f_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='fight',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bouts', to='ufc_events.event'),
        ),
    ]