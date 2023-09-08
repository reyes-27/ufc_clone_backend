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
class FighterProfileAdmin(admin.ModelAdmin):
    list_display = [
        "fighter_slug",
        "full_name",
        "nickname",
        "birthdate",
        "native_city",
        "c_photo",
        "status",
        "fighter_tag",
    ]
    fields = [
        "full_name",
        "nickname",
        "birthdate",
        "native_city",
        "f_photo",
        "c_photo",
        "weight_division",
        "status",
        "fighter_tag",
        "age",
        "reach",
        "height",
        "leg_reach",
        "weight",
        "number_of_fights",
        "victories",
        "losses",
        "draws",
        "no_contest",
    ]

admin.site.register(model_or_iterable=FighterProfile, admin_class=FighterProfileAdmin)
admin.site.register(model_or_iterable=FighterStatus)
admin.site.register(model_or_iterable=FighterTag)
admin.site.register(model_or_iterable=Participation)
admin.site.register(model_or_iterable=Fight)
admin.site.register(model_or_iterable=WeightDivision)