from .serializers import RankingSerializer
from rest_framework.views import APIView
from . models import Ranking
from rest_framework.response import Response
from rest_framework import (
    status,
    permissions,
    )

# Create your views here.

class RankingListView(APIView):
    permission_classes = [permissions.AllowAny,]
    def get(self, request, format=None):
        queryset = Ranking.objects.prefetch_related("ranking_spot").all()
        if Ranking.objects.all().exists():
            serializer = RankingSerializer(queryset, many=True)
            return Response(data={"rankings":serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response(data={"data": "No data"}, status=status.HTTP_204_NO_CONTENT)