from django.urls import path
from . import views
from .views import adoption_application_view
from .views import donation_view, donation_success_view

urlpatterns = [
    path('', views.home, name='home'),
    path('adopt/', views.adopt, name='adopt'),
    path('donate/', views.donate, name='donate'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('pet/<int:pet_id>/', views.pet_detail, name='pet_detail'),
    path('donation/form/', donation_view, name='donation_form'),
    path('adoption-form/', adoption_application_view, name='adoption_form'),
    path('adoption/success/', views.adoption_success_view, name='success'),
    path('donation/success/', views.donation_success_view, name='donation_success'),

]
