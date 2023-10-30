from django.urls import path
from .views import (
    FighterProfileView,
    FightDetailView,
    ParticipationListView,
    )

urlpatterns = [
    path("fighters/<slug:slug>/", view=FighterProfileView.as_view(), name="fighter-detail"),
    path("fights/<int:pk>/", view=FightDetailView.as_view(), name="fight-detail"),
    path("participations/<slug:slug>/", view=ParticipationListView.as_view(), name="participations-list"),
]

