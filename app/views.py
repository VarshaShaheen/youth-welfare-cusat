from django.shortcuts import render, get_object_or_404
from .models import NewsAndEvent, Event


# Create your views here.
def index(request):
    news_and_events = NewsAndEvent.objects.all()
    events = Event.objects.all()
    return render(request, 'app/index.html', {'news_and_events': news_and_events, 'events': events})


def event_detail(request, event_name):
    event = get_object_or_404(Event, name=event_name)
    return render(request, 'app/event_detail.html', {'event': event})
