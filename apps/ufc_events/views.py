from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import (
    Event,
    )
from apps.ufc_base.models import Participation
from .serializers import (
    EventSerializer,
    ShortEventSerializer,
    )
from apps.ufc_base.serializers import ParticipationSerializer
from apps.ufc_base.pagination import SmallSetPagination
# Create your views here.

class EventListView(APIView):
    permission_classes=[permissions.AllowAny,]
    def get(self, request, format=None):
        if Event.objects.all().exists():
            events=Event.objects.all()
            paginator=SmallSetPagination()
            results=paginator.paginate_queryset(events, request=request)
            serializer=ShortEventSerializer(results, many=True, read_only=True, context={"request":request})
            return paginator.get_paginated_response({"events":serializer.data})
        
        else:
            return Response(data={"data":"no events"})
        
class EventDetailView(APIView):
    permission_classes=[permissions.AllowAny,]
    def get(self, request, pk, format=None):
        event=Event.objects.get(id=pk)
        if event:
            serializer=EventSerializer(event, read_only=True, context={"request":request})
            return Response(data={"event":serializer.data})
        
        else:
            return Response(data={"data":"No data <]:{V"})
        

        
class EventTypeView(APIView):
    def get(self, request, format=None):
        return Response(data={"data":"Hiiiii"})
    
