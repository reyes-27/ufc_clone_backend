from django.contrib import admin
from .models import (
    Ranking,
    RankingSpot,
)
# Register your models here.
class RankingAdmin(admin.ModelAdmin):
    exclude = ["ranking_slug",]

admin.site.register(admin_class=RankingAdmin, model_or_iterable=Ranking)
admin.site.register(RankingSpot)