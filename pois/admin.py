from django.contrib import admin
from .models import PointOfInterest



@admin.register(PointOfInterest)
class PointOfInterestAdmin(admin.ModelAdmin):
    list_display = ('id', 'external_id', 'name', 'category', 'get_average_rating')
    search_fields = ('id', 'external_id', 'name')
    readonly_fields = ('external_id',)
    list_filter = ('category',)

    def get_average_rating(self, obj):
        if obj.ratings:
            return sum(obj.ratings) / len(obj.ratings)
        return 'N/A'
    get_average_rating.short_description = 'Avg. rating'
