from rest_framework import serializers
from .models import (
    FighterProfile,
    Participation,
    Fight,
    WeightDivision,

)
from rest_framework.request import Request


class FighterProfileSerializer(serializers.ModelSerializer):

    for field in ['status', 'fighter_tag', 'weight_division']:
        vars()[field] = serializers.CharField()

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

class ShortFighterSerializer(serializers.ModelSerializer):
    # fighter_slug = serializers.HyperlinkedIdentityField(
    #     view_name = "fighter-detail",
    #     lookup_field = "fighter_slug",
    #     lookup_url_kwarg = "slug"
    # )
    # f_photo = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True)
    # c_photo = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True)
    # f_photo = serializers.SerializerMethodField(method_name="get_f_photo_url")
    # c_photo = serializers.SerializerMethodField(method_name="get_c_photo_url")
    class Meta:
        model=FighterProfile
        fields=[
            "fighter_slug",
            "full_name",
            "nickname",
            "f_photo",
            "c_photo",
            "reach",
            "height",
            "leg_reach",
            "weight",
        ]
    # def get_f_photo_url(self, obj):
    #     request=self.context.get("request")
    #     return request.build_absolute_uri(obj.image.url)
    # def get_c_photo_url(self, obj):
    #     request=self.context.get("request")
    #     return request.build_absolute_uri(obj.image.url)
class SuperShortFighterProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FighterProfile
        fields = [
            "fighter_slug",
            "full_name",
            "c_photo",
        ]

class ParticipationSerializer(serializers.ModelSerializer):
    fighter = ShortFighterSerializer(read_only=True)
    class Meta:
        model=Participation
        fields=[
            "fighter",
            "corner",
            "loss",
            "victory",
        ]

class FightSerializer(serializers.ModelSerializer):
    comperitors = ParticipationSerializer(source="fight_to_fighter", many=True, read_only=True)
    class Meta:
        model=Fight
        fields=[
            "id",
            "name",
            "comperitors",
            "number_of_rounds",
            "t_round",
            "status",
            "result",
            "method",
            "card",
            "tier",
        ]

class WeightDivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeightDivision
        fields = [
            "name",
        ]