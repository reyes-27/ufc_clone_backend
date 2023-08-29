from rest_framework.serializers import(
    ModelSerializer,
)
from . import models
# from apps.ufc_events.serializers import (
#     ShortEventSerializer,
#     )


class FighterProfileSerializer(ModelSerializer):
    class Meta:
        model=models.FighterProfile
        fields="__all__"

class ParticipationSerializer(ModelSerializer):
    fighter = FighterProfileSerializer()
    class Meta:
        model=models.Participation
        fields=[
            "corner",
            "fighter",
            "loss",
            "victory",
        ]

class FightSerializer(ModelSerializer):
    fighter_partipation = ParticipationSerializer()
    class Meta:
        model=models.Fight
        fields=[
            "fighter_participation",
            "number_of_rounds",
            "t_round",
            "status",
            "result",
            "method",
        ]
