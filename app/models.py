from django.db import models
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field


class NewsAndEvent(models.Model):
    title = models.CharField(max_length=200)
    last_date_registration = models.DateField()
    details_pdf = models.FileField(upload_to='events/details/')
    registration_link = models.URLField()

    def __str__(self):
        return self.title


class Event(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)  # Allows null and blank values
    cover_image = models.ImageField(upload_to='events/covers/', null=True,
                                    blank=True)  # Null for DB, blank for forms
    description = CKEditor5Field(config_name='extends', null=True, blank=True)
    date = models.CharField(max_length=100, null=True, blank=True)  # Allows null and blank values
    time = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)  # Allows null and blank values
    contact = models.CharField(max_length=100, null=True, blank=True)
    registration_link = models.URLField(max_length=200, null=True, blank=True)  # Allows null and blank values

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('event_detail', kwargs={'event_name': self.name})


class Testimonial(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    position = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='testimonials_images/')
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class NewsItem(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='news_images/')
    description = CKEditor5Field(config_name='extends', null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Director(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='director_image/')
    position = models.CharField(max_length=200, null=True, blank=True)
    about = CKEditor5Field(config_name='extends', null=True, blank=True)
    biodata = models.FileField(upload_to='director/portfolio')
    phone = models.CharField(max_length=200, null=True, blank=True)
    address = CKEditor5Field(config_name='extends', null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    facebook = models.URLField(max_length=200, null=True, blank=True)
    instagram = models.URLField(max_length=200, null=True, blank=True)
    linkedin = models.URLField(max_length=200, null=True, blank=True)
    google = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class CurrentProgramme(models.Model):
    name = models.CharField(max_length=255)
    date = models.CharField(max_length=255, null=True, blank=True)
    time = models.CharField(max_length=255, null=True, blank=True)
    report = models.FileField(upload_to='programme_reports/', null=True, blank=True)  # Assuming PDFs can be optional
    registration_link = models.URLField(max_length=200, null=True, blank=True)
    organisers = models.CharField(max_length=255, null=True, blank=True)
    description = CKEditor5Field(config_name='extends', null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('current_programme_detail', kwargs={'pk': self.pk})


class CampusClubs(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    coordinator = models.CharField(max_length=255, null=True, blank=True)
    mobile = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class NssUnit(models.Model):
    coordinator_name = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return 'nss added'


class Counsellor(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    qualification = models.CharField(max_length=200, null=True, blank=True)
    contact_no = models.CharField(max_length=200, null=True, blank=True)
    office_contact = models.CharField(max_length=200, null=True, blank=True)
    consultation_time = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class AnnualReport(models.Model):
    name = models.CharField(max_length=255)
    report_pdf = models.FileField(upload_to='annual_reports/')

    def __str__(self):
        return self.name


class GraceMarks(models.Model):
    event = models.CharField(max_length=255, null=True, blank=True)
    first = models.CharField(max_length=255, null=True, blank=True)
    second = models.CharField(max_length=255, null=True, blank=True)
    third = models.CharField(max_length=255, null=True, blank=True)
    participation = models.CharField(max_length=255, null=True, blank=True)
    grace_mark_form = models.FileField(upload_to='grace_marks/', null=True)
    uo_grace_mark_form = models.FileField(upload_to='grace_marks/', null=True)

    def __str__(self):
        return self.event


class Program(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    cover_image = models.ImageField(upload_to='program_covers/')

    def __str__(self):
        return self.name


class ProgramImage(models.Model):
    program = models.ForeignKey(Program, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='program_images/')

    def __str__(self):
        return f"{self.program.name} Image"


class Alumni(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    photo = models.ImageField(upload_to='alumni_photos/')

    def __str__(self):
        return self.name


class EssentialInfo(models.Model):
    authority = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    mobile = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.authority


class UniversityOrder(models.Model):
    name = models.CharField(max_length=255)
    order_pdf = models.FileField(upload_to='orders/')

    def __str__(self):
        return self.name


class AntiRagging(models.Model):
    description = models.TextField(max_length=2000, null=True, blank=True)
    order_pdf = models.FileField(upload_to='anti-raggings/')

    def __str__(self):
        return self.description


class StudentAidFund(models.Model):
    description = models.TextField(max_length=2000, null=True, blank=True)
    order_pdf = models.FileField(upload_to='student-aid/')

    def __str__(self):
        return self.description


class Research(models.Model):
    name = models.CharField(max_length=255)
    research_area = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Union(models.Model):
    designation = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=1500, null=True, blank=True)
    contact_number = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.designation


class HealthCenter(models.Model):
    doctor = models.CharField(max_length=255)
    nurse = models.CharField(max_length=255, null=True, blank=True)
    contact_number = models.CharField(max_length=100, null=True, blank=True)
    working_time = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.doctor
