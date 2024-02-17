from django.shortcuts import render, get_object_or_404
from .models import NewsAndEvent, Event, Testimonial, NewsItem, Director, CurrentProgramme, CampusClubs, NssUnit, \
    Counsellor, AnnualReport, GraceMarks, Program, EssentialInfo, UniversityOrder, AntiRagging, StudentAidFund, \
    Research, Union, HealthCentre, Administration, Courses, RadioManagement, RadioJockey, radio_description_and_links


def index(request):
    testimonials = Testimonial.objects.all()
    news_and_events = NewsAndEvent.objects.all().order_by('-created_at')
    events = Event.objects.all().order_by('-created_at')
    news_items = NewsItem.objects.all().order_by('-created_at')
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
    return render(request, 'app/about/department.html')


def about_director(request):
    directors = Director.objects.all()
    return render(request, 'app/about/director.html', {'directors': directors})


def current_program(request):
    programs = CurrentProgramme.objects.all().order_by('-created_at')
    return render(request, 'app/programme/current_program.html', {'programs': programs})


def program_detail(request, pk):
    programme = get_object_or_404(CurrentProgramme, pk=pk)
    return render(request, 'app/programme/program_detail.html', {'programme': programme})


def campus_clubs(request):
    clubs = CampusClubs.objects.all()
    return render(request, 'app/campus/clubs.html', {'clubs': clubs})


def nss_units_view(request):
    units = NssUnit.objects.all()
    return render(request, 'app/campus/nss.html', {'nss_units': units})


def counselling_view(request):
    counsellors = Counsellor.objects.all()
    return render(request, 'app/facilities/counselling.html', {'counsellors': counsellors})


def annual_report_view(request):
    reports = AnnualReport.objects.all().order_by('-created_at')
    return render(request, 'app/annual_report.html', {'reports': reports})


def grace_marks_view(request):
    grace_marks = GraceMarks.objects.all()
    return render(request, 'app/disclosure/grace_marks.html', {'grace_marks': grace_marks})


def program_detail_gallery(request, program_id):
    program = get_object_or_404(Program, pk=program_id)
    return render(request, 'app/gallery/program_details.html', {'program': program})


def program_list(request):
    programs = Program.objects.all().order_by('-created_at')
    return render(request, 'app/gallery/program.html', {'programs': programs})


def contact_us(request):
    directors = Director.objects.all()
    return render(request, 'app/about/contact-us.html', {'directors': directors})


def essential_info(request):
    info = EssentialInfo.objects.all()
    return render(request, 'app/about/essential_info.html', {'info': info})


def feedback(request):
    return render(request, 'app/about/feedback.html')


def show_orders(request):
    orders = UniversityOrder.objects.all()
    return render(request, 'app/disclosure/orders.html', {'orders': orders})


def anti_ragging(request):
    infos = AntiRagging.objects.all()
    return render(request, 'app/disclosure/anti_ragging.html', {'infos': infos})


def student_aid_fund(request):
    infos = StudentAidFund.objects.all()
    return render(request, 'app/scholarships/student-aid.html', {'infos': infos})


def research_view(request):
    researches = Research.objects.all()
    return render(request, 'app/academics/research.html', {'researches': researches})


def union_view(request):
    members = Union.objects.all()
    return render(request, 'app/campus/union.html', {'members': members})


def health_centre_view(request):
    infos = HealthCentre.objects.all()
    return render(request, 'app/facilities/health_centre.html', {'infos': infos})


def administration_view(request):
    infos = Administration.objects.all()
    return render(request, 'app/about/administration.html', {"infos": infos})


def courses_view(request):
    courses = Courses.objects.all()
    return render(request, 'app/academics/courses.html', {'courses': courses})


def radio_view(request):
    managements = RadioManagement.objects.all()
    jockeys = RadioJockey.objects.all()
    details = radio_description_and_links.objects.all()
    return render(request, 'app/campus/radio.html', {'managements': managements, 'details': details, 'jockeys': jockeys})
