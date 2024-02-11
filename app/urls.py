# myapp/urls.py
from django.urls import path
from .views import index, nss_units_view, campus_clubs, counselling_view, annual_report_view
from .views import event_detail, news_detail, about_department, about_director, current_program, program_detail

urlpatterns = [
    path('', index, name='index'),
    path('events/<str:event_name>/', event_detail, name='event_detail'),
    path('<int:pk>/', news_detail, name='news_detail'),
    path('department', about_department, name='department'),
    path('director', about_director, name='director'),
    path('program/current_program', current_program, name='current_program'),
    path('program-detail/<int:pk>/', program_detail, name='program_detail'),
    path('clubs/', campus_clubs, name='clubs'),
    path('nss-units/', nss_units_view, name='nss_units'),
    path('counselling/', counselling_view, name='counselling'),
    path('annual-reports/', annual_report_view, name='annual_reports'),
]
