# Generated by Django 5.0.1 on 2024-02-11 06:39

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_director'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='address',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True),
        ),
    ]