# Generated by Django 5.2.1 on 2025-05-27 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoption', '0012_alter_adoptionapplication_pet_to_adopt'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='illness_description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='pet',
            name='pet_illness',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
