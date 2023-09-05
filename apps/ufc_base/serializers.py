from rest_framework.serializers import(
    ModelSerializer,
)
from .models import (
    FighterProfile,
    Participation,
    Fight,
)
# from apps.ufc_events.serializers import (
#     ShortEventSerializer,
#     )


class FighterProfileSerializer(ModelSerializer):
    class Meta:
        model=FighterProfile
        fields="__all__"

class ShortFighterSerializer(ModelSerializer):
    class Meta:
        model=FighterProfile
        fields=[
            "full_name",
            "nickname",
            "f_photo",
            "c_photo",
            "reach",
            "height",
            "leg_reach",
            "weight",
        ]
class SuperShortFighterProfileSerializer(ModelSerializer):
    class Meta:
        model = FighterProfile
        fields = [
            "full_name",
        ]

class ParticipationSerializer(ModelSerializer):
    fighter = ShortFighterSerializer()
    class Meta:
        model=Participation
        fields=[
            "fighter",
            "corner",
            "loss",
            "victory",
        ]

class FightSerializer(ModelSerializer):
    comperitor = ParticipationSerializer(source="fight_to_fighter", many=True, read_only=True)
    class Meta:
        model=Fight
        fields=[
            "comperitor",
            "number_of_rounds",
            "t_round",
            "status",
            "result",
            "method",
        ]