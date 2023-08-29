from django.db import models
from apps.ufc_base import models as base_models
# Create your models here.

class EventType(models.Model):
    name=               models.CharField(max_length=155)
    ppv =               models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Event(models.Model):
    type_of_event =                 models.ForeignKey(EventType, on_delete=models.PROTECT)
    bout =                          models.ManyToManyField(base_models.Fight, related_name="events")
    name =                          models.CharField(max_length=155)
    description =                   models.TextField()
    
    def __str__(self):
        return self.name