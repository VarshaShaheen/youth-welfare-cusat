# Generated by Django 5.0.1 on 2024-02-16 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0051_radio_management_designation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='radio',
            name='link_to_radio',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='radio',
            name='link_to_youtube',
            field=models.URLField(blank=True, null=True),
        ),
    ]