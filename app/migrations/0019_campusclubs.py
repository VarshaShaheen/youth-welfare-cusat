# Generated by Django 5.0.1 on 2024-02-11 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_currentprogramme_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampusClubs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('coordinator', models.CharField(blank=True, max_length=255, null=True)),
                ('mobile', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
