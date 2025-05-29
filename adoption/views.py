import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignupForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Profile, Pet
from .forms import AdoptionApplicationForm
from django.conf import settings
from .forms import DonationForm

def home(request):
    context = {
        'timestamp': timezone.now().timestamp()
    }
    return render(request, 'adoption/home.html', context)

def home(request):
    return render(request, 'adoption/home.html')

def adopt(request):
    filter_type = request.GET.get('filter')
    if filter_type == 'cats':
        pets = Pet.objects.filter(type='cat')
    elif filter_type == 'dogs':
        pets = Pet.objects.filter(type='dog')
    else:
        pets = Pet.objects.all()
    return render(request, 'adoption/adopt.html', {'pets': pets, 'filter': filter_type})

@login_required
def donate(request):
    return render(request, 'adoption/donate.html')

def login_view(request):
    """ Login page view """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'adoption/login.html', {'form': form})

def logout_view(request):
    """ Logout the user and redirect to home page """
    logout(request)
    return redirect('home')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Automatically log in the user after successful signup
            login(request, user)
            return redirect('home')  # Redirect to home page after successful signup
        else:
            print("Form errors:", form.errors)
    else:
        form = SignupForm()

    return render(request, 'adoption/signup.html', {'form': form}) 

def pet_detail(request, pet_id):
    """ Pet detail view - Fetch pet from the database """
    # Fetch the pet object using the ID or show a 404 page if not found
    pet = get_object_or_404(Pet, id=pet_id)
    return render(request, 'adoption/pet_detail.html', {'pet': pet})

@login_required
def adoption_application_view(request):
    if request.method == 'POST':
        form = AdoptionApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')  # Or wherever you want
    else:
        form = AdoptionApplicationForm()
    return render(request, 'adoption/adoption_form.html', {'form': form})

def adoption_success_view(request):
    return render(request, 'adoption/success.html')

@login_required
def donation_view(request):
    if request.method == 'POST':
        form = DonationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('donation_success')
    else:
        form = DonationForm()
    return render(request, 'adoption/donation_form.html', {'form': form})

def donation_success_view(request):
    return render(request, 'adoption/donation_success.html')