from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    ModelSerializer,
)
from apps.ufc_base.serializers import (
    SuperShortFighterProfileSerializer,
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
    ranking_spot = RankingSpotSerializer(source="ranking_to_fighter", many=True, read_only=True)
    class Meta:
        model = Ranking
        fields = [
            "weight_division",
            "ranking_spot"
        ]