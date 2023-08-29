from rest_framework import serializers
from . import models
from apps.ufc_base.serializers import FightSerializer

class EventSerializer(serializers.HyperlinkedModelSerializer):
    
    url=serializers.HyperlinkedIdentityField(
        view_name="event-detail",
        lookup_field="id",
        lookup_url_kwarg="pk",
    )

    type_of_event=serializers.CharField()

    bout = FightSerializer(many=True, read_only=True)

    class Meta:
        model = models.Event
        fields = [
            "url",
            "id",
            "type_of_event",
            "bout",
            "name",
            "description",
        ]

class ShortEventSerializer(serializers.HyperlinkedModelSerializer):
    url=serializers.HyperlinkedIdentityField(
        view_name="event-detail",
        lookup_field="id",
        lookup_url_kwarg="pk",
    )
    class Meta:
        model=models.Event
        fields=[
            "url",
            "id",
            "name",
        ] 