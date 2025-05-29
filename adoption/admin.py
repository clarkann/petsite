from django.contrib import admin
from .models import Profile
from .models import Pet
from .models import AdoptionApplication
from .models import Donation

class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'breed', 'image_preview')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="100" height="100" />'
        return "No Image"
    image_preview.allow_tags = True
    image_preview.short_description = "Image Preview"

admin.site.register(Pet, PetAdmin)

admin.site.register(Profile)

@admin.register(AdoptionApplication)
class AdoptionApplicationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'pet_preference', 'zoom_date', 'get_pet_illness')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('pet_preference', 'status', 'pronouns', 'residence_type', 'zoom_date')

    def get_pet_illness(self, obj):
        return obj.pet.pet_illness if obj.pet else 'N/A'
    get_pet_illness.short_description = 'Pet Illness'

admin.site.register(Donation)
