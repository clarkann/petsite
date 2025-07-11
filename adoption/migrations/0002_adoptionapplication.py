# Generated by Django 5.2.1 on 2025-05-15 07:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoption', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdoptionApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('birth_date', models.DateField()),
                ('occupation', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('social_media_profile', models.URLField(blank=True)),
                ('status', models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Others', 'Others')], max_length=10)),
                ('pronouns', models.CharField(choices=[('She/her', 'She/her'), ('He/him', 'He/him'), ('They/them', 'They/them')], max_length=10)),
                ('adoption_reason', models.TextField()),
                ('has_adopted_before', models.BooleanField()),
                ('alt_first_name', models.CharField(max_length=100)),
                ('alt_last_name', models.CharField(max_length=100)),
                ('alt_relationship', models.CharField(max_length=50)),
                ('alt_phone', models.CharField(max_length=20)),
                ('alt_email', models.EmailField(max_length=254)),
                ('pet_preference', models.CharField(choices=[('Cat', 'Cat'), ('Dog', 'Dog'), ('Both', 'Both'), ('Not decided', 'Not decided')], max_length=20)),
                ('specific_pet', models.BooleanField()),
                ('pet_description', models.TextField()),
                ('residence_type', models.CharField(choices=[('House', 'House'), ('Apartment', 'Apartment'), ('Condo', 'Condo'), ('Other', 'Other')], max_length=20)),
                ('rent', models.BooleanField()),
                ('plan_for_moving', models.TextField()),
                ('living_with', models.TextField()),
                ('allergies', models.BooleanField()),
                ('pet_care_responsibility', models.TextField()),
                ('financial_responsibility', models.TextField()),
                ('pet_care_backup', models.TextField()),
                ('pet_alone_hours', models.IntegerField()),
                ('pet_introduction_plan', models.TextField()),
                ('family_support', models.BooleanField()),
                ('family_explanation', models.TextField()),
                ('other_pets', models.BooleanField()),
                ('past_pets', models.BooleanField()),
                ('home_photos', models.FileField(blank=True, upload_to='adoption_photos/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'png', 'jpeg'])])),
                ('valid_id', models.FileField(upload_to='ids/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'png', 'jpeg', 'pdf'])])),
                ('zoom_date', models.DateField()),
                ('zoom_time', models.TimeField()),
                ('shelter_visit', models.BooleanField()),
            ],
        ),
    ]
