# Generated by Django 5.0.1 on 2024-02-11 09:25

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_currentprogramme_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='currentprogramme',
            name='description',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True),
        ),
    ]
