# Generated by Django 5.0.1 on 2024-02-15 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0046_administration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(blank=True, max_length=255, null=True)),
                ('details', models.FileField(upload_to='courses/')),
            ],
        ),
        migrations.AddField(
            model_name='healthcentre',
            name='office_contact',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='healthcentre',
            name='qualification',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
