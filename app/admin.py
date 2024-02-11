from django.contrib import admin
from .models import NewsAndEvent, Event, Testimonial, NewsItem, Director, CurrentProgramme, CampusClubs, NssUnit, \
    Counsellor, AnnualReport


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


@admin.register(CampusClubs)
class CampusClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'coordinator')


@admin.register(NssUnit)
class NssUnitAdmin(admin.ModelAdmin):
    list_display = ('unit_no', 'college_department')


@admin.register(Counsellor)
class CounsellorAdmin(admin.ModelAdmin):
    list_display = ('name', 'qualification')


@admin.register(AnnualReport)
class AnnualReportAdmin(admin.ModelAdmin):
    list_display = ('name',)
