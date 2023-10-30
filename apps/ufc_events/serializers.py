from rest_framework import serializers
from . import models
from apps.ufc_base.serializers import FightSerializer

class EventSerializer(serializers.HyperlinkedModelSerializer):
    
    url=serializers.HyperlinkedIdentityField(
        view_name="event-detail",
        lookup_field="id",
        lookup_url_kwarg="pk",
    )
    
    type_of_event = serializers.CharField()
    bouts = serializers.SerializerMethodField()

    class Meta:
        model = models.Event
        fields = [
            "url",
            "id",
            "cover",
            "type_of_event",
            "bouts",
            "name",
            "description",
            "status",
        ]

    def get_bouts(self, instance):
        bouts = instance.bout.order_by("card", "tier")
        return FightSerializer(bouts, many=True, read_only=True).data
    
        


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
            "cover",
            "name",
            "description",
            "status",

        ] 