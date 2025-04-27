from django.contrib import admin
from .models import Incident

@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'severity', 'reported_at')
    search_fields = ('title', 'description')
    list_filter = ('severity',)
