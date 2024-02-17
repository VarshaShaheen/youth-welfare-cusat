from django.contrib import admin
from .models import NewsAndEvent, Event, Testimonial, NewsItem, Director, CurrentProgramme, CampusClubs, NssUnit, \
    Counsellor, AnnualReport, GraceMarks, Alumni, EssentialInfo, UniversityOrder, Program, ProgramImage, AntiRagging, \
    StudentAidFund, Research, Union, HealthCentre, Administration, Courses, RadioManagement, RadioJockey, radio_description_and_links


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
    list_display = ('coordinator_name',)


@admin.register(Counsellor)
class CounsellorAdmin(admin.ModelAdmin):
    list_display = ('name', 'qualification')


@admin.register(AnnualReport)
class AnnualReportAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(GraceMarks)
class GraceMarkAdmin(admin.ModelAdmin):
    list_display = ('event',)


class ProgramImageInline(admin.TabularInline):
    model = ProgramImage
    extra = 1


class ProgramAdmin(admin.ModelAdmin):
    inlines = [ProgramImageInline, ]


admin.site.register(Program, ProgramAdmin)
admin.site.register(ProgramImage)


@admin.register(Alumni)
class AlumniAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(EssentialInfo)

admin.site.register(UniversityOrder)

admin.site.register(AntiRagging)

admin.site.register(StudentAidFund)

admin.site.register(Research)


@admin.register(Union)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ('designation', 'name')


@admin.register(HealthCentre)
class HealthCentreAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Administration)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('course',)


admin.site.register(RadioManagement)
admin.site.register(RadioJockey)
admin.site.register(radio_description_and_links)