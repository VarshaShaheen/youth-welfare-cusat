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
    twitter = models.URLField(max_length=200, null=True, blank=True)
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
