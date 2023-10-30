# Generated by Django 4.2.4 on 2023-09-15 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ufc_base', '0008_alter_fight_options_alter_fight_card_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fight',
            name='card',
            field=models.CharField(blank=True, choices=[(0, 'MAIN CARD'), (1, 'PRELIMS'), (2, 'EARLY PRELIMS')], max_length=155, null=True),
        ),
        migrations.AlterField(
            model_name='fight',
            name='tier',
            field=models.CharField(blank=True, choices=[(0, 'fight-0'), (1, 'fight-1'), (2, 'fight-2'), (3, 'fight-3'), (4, 'fight-4')], max_length=155, null=True),
        ),
    ]
