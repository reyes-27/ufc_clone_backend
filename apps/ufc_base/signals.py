from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Participation
from django.utils.text import slugify

@receiver(post_save, sender=Participation)
def participation_signals(sender, created, instance, **kwargs):
    if not created:
        if instance.victory == True:
            instance.loss = False
            instance.fighter.victories += 1
        elif instance.loss == True:
            instance.victory = False
            instance.fighter.losses += 1
    print(instance.fighter.losses)