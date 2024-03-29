# Generated by Django 5.0.1 on 2024-02-12 09:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_alter_gracemarks_first_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('cover_image', models.ImageField(upload_to='program_covers/')),
            ],
        ),
        migrations.CreateModel(
            name='ProgramImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='program_images/')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='app.program')),
            ],
        ),
    ]
