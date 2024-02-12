from django.shortcuts import render, get_object_or_404
from .models import NewsAndEvent, Event, Testimonial, NewsItem, Director, CurrentProgramme, CampusClubs, NssUnit, \
    Counsellor, AnnualReport, GraceMarks, Program, Alumni


def index(request):
    testimonials = Testimonial.objects.all()
    news_and_events = NewsAndEvent.objects.all()
    events = Event.objects.all()
    news_items = NewsItem.objects.all().order_by('-date_posted')
    return render(request, 'app/index.html',
                  {'news_and_events': news_and_events, 'events': events, 'testimonials': testimonials,
                   'news_items': news_items})


def event_detail(request, event_name):
    event = get_object_or_404(Event, name=event_name)
    return render(request, 'app/event_detail.html', {'event': event})


def news_detail(request, pk):
    news_item = get_object_or_404(NewsItem, pk=pk)
    return render(request, 'app/news_detail.html', {'news_item': news_item})


def about_department(request):
    return render(request, 'app/department.html')


def about_director(request):
    directors = Director.objects.all()
    return render(request, 'app/director.html', {'directors': directors})


def current_program(request):
    programs = CurrentProgramme.objects.all()
    return render(request, 'app/programme/current_program.html', {'programs': programs})


def program_detail(request, pk):
    programme = get_object_or_404(CurrentProgramme, pk=pk)
    return render(request, 'app/programme/program_detail.html', {'programme': programme})


def campus_clubs(request):
    clubs = CampusClubs.objects.all()
    return render(request, 'app/campus_activities/clubs.html', {'clubs': clubs})


def nss_units_view(request):
    units = NssUnit.objects.all()
    return render(request, 'app/campus_activities/nss.html', {'nss_units': units})


def counselling_view(request):
    counsellors = Counsellor.objects.all()
    return render(request, 'app/other/counselling.html', {'counsellors': counsellors})


def annual_report_view(request):
    reports = AnnualReport.objects.all()
    return render(request, 'app/annual_report.html', {'reports': reports})


def grace_marks_view(request):
    grace_marks = GraceMarks.objects.all()
    return render(request, 'app/academics/grace_marks.html', {'grace_marks': grace_marks})


def program_detail_gallery(request, program_id):
    program = get_object_or_404(Program, pk=program_id)
    return render(request, 'app/gallery/program_details.html', {'program': program})


def program_list(request):
    programs = Program.objects.all()
    return render(request, 'app/gallery/program.html', {'programs': programs})


def alumni_list(request):
    alumnis = Alumni.objects.all()
    return render(request, 'app/about/alumni.html', {'alumnis': alumnis})
