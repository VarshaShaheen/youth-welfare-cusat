# Generated by Django 5.0.1 on 2024-02-11 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_campusclubs'),
    ]

    operations = [
        migrations.CreateModel(
            name='NssUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_no', models.CharField(max_length=50)),
                ('college_department', models.CharField(max_length=200)),
                ('programme_officer', models.CharField(max_length=200)),
                ('secretary', models.CharField(max_length=200)),
            ],
        ),
    ]
