# Generated by Django 5.0.1 on 2024-02-11 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_alter_counsellor_contact_no_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnualReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('report_pdf', models.FileField(upload_to='annual_reports/')),
            ],
        ),
    ]