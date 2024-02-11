from django.contrib import admin
from .models import NewsAndEvent, Event, Testimonial, NewsItem, Director, CurrentProgramme


@admin.register(NewsAndEvent)
class NewsAndEventAdmin(admin.ModelAdmin):
    list_display = ('title', 'last_date_registration')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')


@admin.register(NewsItem)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted')


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')


@admin.register(CurrentProgramme)
class CurrentProgrammeAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')
