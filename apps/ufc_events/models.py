from django.db import models
from apps.ufc_base import models as base_models
from django_resized import ResizedImageField
import uuid
from django.utils.text import slugify
# Create your models here.

class EventType(models.Model):
    name=               models.CharField(max_length=155)
    ppv =               models.BooleanField(default=False)
    def __str__(self):
        return self.name

def event_cover(instance, filename):
    instance = slugify(instance)
    ext = filename.split(".")[-1]
    uuid_name = uuid.uuid4()
    filename = f'{uuid_name}.{ext}'
    return f'events/covers/{instance}/{filename}'
class Event(models.Model):
    status_choices = (
        ("CE", "CANCELLED"),
        ("UP", "UPCOMING"),
        ("FT", "FOUGHT"),
    )
    type_of_event =                 models.ForeignKey(EventType, on_delete=models.PROTECT)
    bout =                          models.ManyToManyField(base_models.Fight, related_name="events")
    cover =                         ResizedImageField(upload_to=event_cover, force_format='PNG', blank=True, null=True)
    name =                          models.CharField(max_length=155)
    description =                   models.TextField()
    status =                        models.CharField(max_length=155, choices=status_choices, default="UP")

    @staticmethod
    def get_events_by_status(status):
        return Event.objects.filter(status=status)

    def __str__(self):
        return self.name