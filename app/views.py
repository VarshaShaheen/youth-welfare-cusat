from django.shortcuts import render, get_object_or_404
from .models import NewsAndEvent, Event, Testimonial, NewsItem, Director


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
