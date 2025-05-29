from rest_framework import serializers 
from adoption.models import Pet, AdoptionApplication

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ['id', 'name', 'age', 'breed', 'image', 'description']

class AdoptionApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdoptionApplication
        fields = [
            'first_name',
            'last_name',
            'address',
            'phone',
            'email',
            'birth_date',
            'social_media_profile',
            'status',
            'pronouns',
            'adoption_reason',
            'pet_preference',
            'specific_pet',
            'pet_to_adopt',
            'residence_type',
            'rent',
            'living_with',
            'allergies',
            'pet_care_responsibility',
            'financial_responsibility',
            'pet_introduction_plan',
            'other_pets',
            'past_pets',
            'home_photos',
            'valid_id',
            'zoom_date',
            'zoom_time',
            'shelter_visit',
        ]
