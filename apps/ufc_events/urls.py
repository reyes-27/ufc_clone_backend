from django.urls import path
from .views import (
    EventListView,
    EventDetailView,
    EventTypeView,
    )

urlpatterns = [
    path("", view=EventListView.as_view(), name="event-list"),
    path("<int:pk>/", view=EventDetailView.as_view(), name="event-detail"),
    path("type/<int:pk>/", view=EventTypeView.as_view(), name="event-type-detail"),
]
