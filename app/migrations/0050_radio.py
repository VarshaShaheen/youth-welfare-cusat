# Generated by Django 5.0.1 on 2024-02-16 17:35

import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0049_currentprogramme_created_at_event_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Radio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True)),
            ],
        ),
    ]
