# myapp/urls.py
from django.urls import path
from .views import index
from .views import event_detail, news_detail


urlpatterns = [
    path('', index, name='index'),
    path('events/<str:event_name>/', event_detail, name='event_detail'),
    path('<int:pk>/', news_detail, name='news_detail'),
]
