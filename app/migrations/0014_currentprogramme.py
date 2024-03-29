# Generated by Django 5.0.1 on 2024-02-11 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_director_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentProgramme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('report', models.FileField(blank=True, null=True, upload_to='programme_reports/')),
                ('registration_link', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
