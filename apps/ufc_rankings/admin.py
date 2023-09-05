from django.contrib import admin
from .models import (
    Ranking,
    RankingSpot,
)
# Register your models here.

admin.site.register(Ranking)
admin.site.register(RankingSpot)