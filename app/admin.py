from django.contrib import admin
from .models import NewsAndEvent, Event


@admin.register(NewsAndEvent)
class NewsAndEventAdmin(admin.ModelAdmin):
    list_display = ('title', 'last_date_registration')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')