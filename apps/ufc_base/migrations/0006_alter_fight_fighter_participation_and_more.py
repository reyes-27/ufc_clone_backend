# Generated by Django 4.2.4 on 2023-09-03 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ufc_base', '0005_alter_fight_fighter_participation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fight',
            name='fighter_participation',
            field=models.ManyToManyField(through='ufc_base.Participation', to='ufc_base.fighterprofile'),
        ),
        migrations.AlterField(
            model_name='participation',
            name='fight',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fight_to_fighter', to='ufc_base.fight'),
        ),
        migrations.AlterField(
            model_name='participation',
            name='fighter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fighter_to_fight', to='ufc_base.fighterprofile'),
        ),
    ]
