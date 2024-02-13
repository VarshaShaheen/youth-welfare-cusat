# myapp/urls.py
from django.urls import path
from .views import index, nss_units_view, campus_clubs, counselling_view, annual_report_view, grace_marks_view, \
    program_list, alumni_list, event_detail, news_detail, about_department, about_director, current_program, \
    program_detail, program_detail_gallery, contact_us, essential_info, feedback, show_orders, anti_ragging


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
    path('grace-marks/', grace_marks_view, name='grace_marks'),
    path('program/<int:program_id>/', program_detail_gallery, name='program_detail'),
    path('program/', program_list, name='program_list'),
    path('about/alumni/', alumni_list, name='alumni_list'),
    path('about/contact-us', contact_us, name='contact_us'),
    path('about/essential-info', essential_info, name='essential_info'),
    path('about/feedback', feedback, name='feedback'),
    path('disclosure/orders', show_orders, name='show_orders'),
    path('disclosure/anti-ragging', anti_ragging, name='anti_ragging'),

]
