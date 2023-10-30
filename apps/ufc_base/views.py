from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework import (
    permissions,
    status,
)
from rest_framework.views import APIView
from .models import (
    Fight,
    FighterProfile,
    Participation,
)
from .serializers import (
    FightSerializer,
    FighterProfileSerializer,
    ParticipationSerializer,
)


# Create your views here.

class FightDetailView(RetrieveAPIView):
    permission_classes = [permissions.AllowAny, ]

    def get_object(self):
        object = Fight.objects.get(pk=self.kwargs["pk"])
        return object

    def get(self, request, format=None, *args, **kwargs):
        fight = self.get_object()
        serializer = FightSerializer(fight, read_only=True)
        return Response(data={"data": serializer.data})


class FighterProfileView(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request, format=None, *args, **kwargs):
        profile = FighterProfile.objects.get(fighter_slug=self.kwargs["slug"])
        if profile:
            serializer = FighterProfileSerializer(profile, context={"request": request})
            return Response(data={"fighter": serializer.data})
        else:
            return Response(data={"fighter": "nothing"})


class ParticipationListView(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request, *args, **kwargs):
        fighter = FighterProfile.objects.get(fighter_slug=self.kwargs["slug"])
        fights = Fight.objects.filter(fighter_participation=fighter)
        if fights:
            serializer = FightSerializer(instance=fights, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data={"data": "No participations"}, status=status.HTTP_204_NO_CONTENT)
