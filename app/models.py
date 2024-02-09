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
    description = CKEditor5Field(config_name='extends', null=True,blank=True)
    date = models.CharField(max_length=100, null=True, blank=True)  # Allows null and blank values
    time = models.CharField(max_length=100,null=True,blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)  # Allows null and blank values
    contact = models.CharField(max_length=100, null=True, blank=True)
    registration_link = models.URLField(max_length=200, null=True, blank=True)  # Allows null and blank values

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('event_detail', kwargs={'event_name': self.name})
