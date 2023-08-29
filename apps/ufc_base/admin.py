from django.contrib import admin
from .models import (
    FighterProfile,
    FighterStatus,
    FighterTag,
    Fight,
    WeightDivision,
    Participation,
)
# Register your models here.

admin.site.register(model_or_iterable=FighterProfile)
admin.site.register(model_or_iterable=FighterStatus)
admin.site.register(model_or_iterable=FighterTag)
admin.site.register(model_or_iterable=Participation)
admin.site.register(model_or_iterable=Fight)
admin.site.register(model_or_iterable=WeightDivision)