# Generated by Django 5.0.1 on 2024-02-13 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_universityorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='AntiRagging',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('order_pdf', models.FileField(upload_to='anti-raggings/')),
            ],
        ),
    ]
