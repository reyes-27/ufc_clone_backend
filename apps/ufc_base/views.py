from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework import permissions
from rest_framework.views import APIView
from .models import (
    Fight,
    FighterProfile,
)
from .serializers import (
    FightSerializer,
    FighterProfileSerializer,
    )
# Create your views here.

class FightDetailView(RetrieveAPIView):
    permission_classes=[permissions.AllowAny,]
    def get_object(self):
        object=Fight.objects.get(pk=self.kwargs["pk"])
        return object
    def get(self, request, format=None, *args, **kwargs):
        fight=self.get_object()
        print(fight, "--------------------")
        serializer=FightSerializer(fight, read_only=True)
        return Response(data={"data":serializer.data})
    
class FighterProfileView(APIView):
    permission_classes=[permissions.AllowAny,]
    def get(self, request, format=None, *args, **kwargs):
        profile=FighterProfile.objects.get(pk=self.kwargs["pk"])
        if profile:
            serializer=FighterProfileSerializer(profile)
            return Response(data={"data":serializer.data})
        else:
            return Response(data={"data":"nothing"})