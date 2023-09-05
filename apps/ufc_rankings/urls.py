from django.urls import path
from .views import RankingListView
urlpatterns = [
    path("", view=RankingListView.as_view(), name="rankings_listview"),
]
