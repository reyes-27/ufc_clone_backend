from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    ModelSerializer,
)
from apps.ufc_base.serializers import (
    SuperShortFighterProfileSerializer,
    WeightDivisionSerializer,
)

from .models import (
    Ranking,
    RankingSpot,
    )

#----------------------------SERIALIZERS----------------------------


class RankingSpotSerializer(ModelSerializer):
    fighter = SuperShortFighterProfileSerializer()
    class Meta:
        model = RankingSpot
        fields = [
            "fighter",
            "rank_number",
            "champion",
            "interm_champion",
        ]

class RankingSerializer(ModelSerializer):
    fighters = RankingSpotSerializer(source="ranking_to_fighter", many=True, read_only=True)
    weight_division = WeightDivisionSerializer()
    class Meta:
        model = Ranking
        fields = [
            "weight_division",
            "fighters"
        ]