# Generated by Django 5.0.1 on 2024-02-19 04:22

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0058_delete_alumni'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
