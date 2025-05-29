from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PetViewSet, AdoptionApplicationViewSet

router = DefaultRouter()
router.register(r'pets', PetViewSet)
router.register(r'adoptionapplication', AdoptionApplicationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
