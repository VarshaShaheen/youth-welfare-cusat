# myapp/urls.py
from django.urls import path
from .views import index
from .views import event_detail


urlpatterns = [
    path('', index, name='index'),
    path('events/<str:event_name>/', event_detail, name='event_detail'),
]
