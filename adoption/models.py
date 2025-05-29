from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import FileExtensionValidator
from django.db import IntegrityError

class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(default="Not provided")
    
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    This function creates or updates a Profile instance whenever a User instance is created or updated.
    """
    try:
        profile, created = Profile.objects.get_or_create(user=instance)
        # If profile already exists, update additional fields as needed
        if not created:
            profile.email = instance.email
            profile.address = profile.address if profile.address else "Not provided"
            profile.phone = profile.phone if profile.phone else ""
            profile.save()
    except IntegrityError:
        # Handle potential integrity errors in case of duplicate profiles
        profile = Profile.objects.get(user=instance)
        profile.email = instance.email
        profile.save()

# --- Adoption Application Model Example ---
class AdoptionApplication(models.Model):
    PET_CHOICES = [
    ('Tiger', 'Tiger'),
    ('Tiny Terror', 'Tiny Terror'),
    ('Pinpin', 'Pinpin'),
    # Add more pet names as needed
]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    birth_date = models.DateField()
    social_media_profile = models.URLField(blank=True)
    status = models.CharField(max_length=10, choices=[('Single', 'Single'), ('Married', 'Married'), ('Others', 'Others')])
    pronouns = models.CharField(max_length=10, choices=[('She/her', 'She/her'), ('He/him', 'He/him')])
    adoption_reason = models.TextField()
    pet_preference = models.CharField(max_length=20, choices=[('Cat', 'Cat'), ('Dog', 'Dog'), ('Both', 'Both'), ('Not decided', 'Not decided')])
    specific_pet = models.BooleanField()
    pet_to_adopt = models.CharField(max_length=100, choices=PET_CHOICES, default='Tiger')
    residence_type = models.CharField(max_length=20, choices=[('House', 'House'), ('Apartment', 'Apartment'), ('Condo', 'Condo'), ('Other', 'Other')])
    rent = models.BooleanField()
    living_with = models.TextField()
    allergies = models.BooleanField()
    pet_care_responsibility = models.TextField()
    financial_responsibility = models.TextField()
    pet_introduction_plan = models.TextField()
    other_pets = models.BooleanField()
    past_pets = models.BooleanField()
    home_photos = models.FileField(upload_to='adoption_photos/', validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])], blank=True)
    valid_id = models.FileField(upload_to='ids/', validators=[FileExtensionValidator(['jpg', 'png', 'jpeg', 'pdf'])])
    zoom_date = models.DateField()
    zoom_time = models.TimeField()
    shelter_visit = models.BooleanField()

    def __str__(self):
        return f"Adoption Application - {self.first_name} {self.last_name}"

class Pet(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(max_length=100, default='Unknown')
    weight = models.FloatField(default=0.0)
    WEIGHT_UNIT_CHOICES = [('kg', 'Kilograms'), ('lb', 'Pounds')]
    weight_unit = models.CharField(max_length=2, choices=WEIGHT_UNIT_CHOICES, default='kg')
    breed = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=[('cat', 'Cat'), ('dog', 'Dog')])
    pet_illness = models.CharField(max_length=100, blank=True)
    illness_description = models.TextField(blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='pet_images/', blank=True, null=True)

    def __str__(self):
        return self.name

class Donation(models.Model):
    donor_name = models.CharField(max_length=100)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    cause = models.CharField(max_length=50, choices=[
        ('Neutering', 'Neutering'),
        ('Shelter', 'Shelter'),
        ('Food', 'Food'),
        ('General', 'General'),
    ])
    receipt = models.FileField(upload_to='donation_receipts/', validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'pdf'])], blank=True)

    def __str__(self):
        return f"{self.donor_name} - {self.amount} for {self.cause}"
