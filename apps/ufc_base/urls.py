from django.urls import path
from .views import (
    FighterProfileView,
    FightDetailView,
    )

urlpatterns = [
    path("fighters/<int:pk>/", view=FighterProfileView.as_view(), name="fighter-detail"),
    path("fight/<int:pk>/",view=FightDetailView.as_view(), name="fight-detail"),
]
