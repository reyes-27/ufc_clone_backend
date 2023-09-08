from rest_framework.serializers import(
    ModelSerializer,
)
from .models import (
    FighterProfile,
    Participation,
    Fight,
    WeightDivision,
)
# from apps.ufc_events.serializers import (
#     ShortEventSerializer,
#     )


class FighterProfileSerializer(ModelSerializer):
    class Meta:
        model=FighterProfile
        fields=[
            "fighter_slug",
            "full_name",
            "nickname",
            "birthdate",
            "native_city",
            "f_photo",
            "c_photo",
            "weight_division",
            "status",
            "fighter_tag",
            "age",
            "reach",
            "height",
            "leg_reach",
            "weight",
            "number_of_fights",
            "victories",
            "losses",
            "draws",
            "no_contest",
        ]

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

class WeightDivisionSerializer(ModelSerializer):
    class Meta:
        model = WeightDivision
        fields = [
            "name",
        ]