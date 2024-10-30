from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login
from users.models import User, Barber, Profile
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from services.models import Services
from rest_framework import viewsets
from django.contrib import messages
from salons.models import Salon
from .serializers import *
from .models import *



# API üçün ViewSet-lər
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BarberViewSet(viewsets.ModelViewSet):
    queryset = Barber.objects.all()
    serializer_class = BarberSerializer

class SosialLinksViewSet(viewsets.ModelViewSet):
    queryset = SosialLinks.objects.all()
    serializer_class = SosialLinksSerializer


# İstifadəçi daxil olma
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            # JWT tokenləri yaradın
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            response = redirect('home')
            response.set_cookie('access_token', access_token, httponly=True, secure=True, samesite='Lax')
            response.set_cookie('refresh_token', refresh_token, httponly=True, secure=True, samesite='Lax')
            
            return response
        else:
            messages.error(request, 'Yanlış istifadəçi adı və ya şifrə.')
    
    return render(request, 'users/login_user.html')

def register_salon(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        services = request.POST.getlist('services')
        barbers = request.POST.get('barbers')
        sosial_links = request.POST.get('sosial_links')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        image = request.FILES.get('image')
        description = request.POST.get('description')
        # İstifadəçi adı yoxlanması
        if not name:
            messages.error(request, 'Salon adı daxil edilmelidir.')
        # Şifrələrin uyğunluğunu yoxlama
        if password!=confirm_password:
            messages.error(request, 'Şifrələr uyğun deyil.')
            return render(request, 'users/register_salon.html')
        
        if Salon.objects.filter(name=name).exists():
            messages.error(request, 'Bu salon adı artıq mövcuddur.')
            return render(request, 'users/register_salon.html')
        
        salon = Salon(name=name, address=address, phone_number=phone)
        salon.set_password(password)
        salon.name = name
        salon.save()

        for service in services:
            services_obj = Services.objects.get(id=service)
            salon.services.add(services_obj)
        
        if barbers:
            barber_obj = Barber.objects.get(id=barbers)
            salon.barbers = barber_obj
        profile = Profile.objects.create(
            name=profile,
            adress = adress,
            phone = phone,
            services = services,
            sosial_links = sosial_links,
            image = image,
            description = description,

        )
        messages.success(request, 'Qeydiyyat uğurla tamamlandı.')
        return redirect('home')
    
    return render(request, 'users/register_salon.html')       

def register_barber(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        birth_date = request.POST.get('birth_date')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        barber_name = request.POST.get('barber_name')
        services_barber = request.POST.get('services_barber') 
        adress = request.POST.get('adress')       
        # İstifadəçi adı yoxlanması
        if not username:
            messages.error(request, 'İstifadəçi adi daxil edilmelidir.')
        # E-mail yoxlanması
        if not email:
            messages.error(request, 'E-mail daxil edilməlidir.')
            return render(request, 'users/register_barber.html')
        # Şifrələrin uyğunluğunu yoxlama
        if password != confirm_password:
            messages.error(request, 'Şifrələr uyğun deyil.')
            return render(request, 'users/register_barber.html')
        
        if Barber.objects.filter(username=username).exists():
            messages.error(request, 'Bu Barber adı artıq mövcuddur.')
            return render(request, 'users/register_barber.html')

        barber = Barber(username=username, email=email)
        barber.set_password(password)  # Şifrəni burada təyin edirik
        barber.first_name = first_name  # Adı burada təyin edirik
        barber.last_name = last_name  # Soyadı burada təyin edirik
        barber.save()  # İstifadəçini bazaya əlavə edirik


        profile = Profile.objects.create(
            barber=barber, 
            phone=phone,
            services_barber=services_barber,
            adress=adress,  
        )
        messages.success(request, 'Qeydiyyat uğurla tamamlandı.')
        return redirect('home')
    
    return render(request, 'users/register_barber.html')
        
def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        birth_date = request.POST.get('birth_date')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        # İstifadəçi adı yoxlanması
        if not username:
            messages.error(request, 'İstifadəçi adı daxil edilməlidir.')
            return render(request, 'users/register_user.html')
        
        # E-mail yoxlanması
        if not email:
            messages.error(request, 'E-mail daxil edilməlidir.')
            return render(request, 'users/register_user.html')
        
        # Şifrələrin uyğunluğunu yoxlama
        if password != confirm_password:
            messages.error(request, 'Şifrələr uyğun deyil.')
            return render(request, 'users/register_user.html')

        # İstifadəçi adı artıq mövcuddur mu?
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Bu istifadəçi adı artıq mövcuddur.')
            return render(request, 'users/register_user.html')

        # İstifadəçini yarat
        user = User(username=username, email=email)
        user.set_password(password)  # Şifrəni burada təyin edirik
        user.first_name = first_name  # Adı burada təyin edirik
        user.last_name = last_name  # Soyadı burada təyin edirik
        user.save()  # İstifadəçini bazaya əlavə edirik
        
        # Profili yarat
        profile = Profile.objects.create(
            user=user,  # Burada 'user' obyektini veririk
            phone=phone, 
            gender=gender, 
            birth_date=birth_date
        )

        messages.success(request, 'Qeydiyyat uğurla tamamlandı.')
        return redirect('home')
    
    return render(request, 'users/register_user.html')


# Profilin redaktə olunması
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profiliniz uğurla yeniləndi.')
            return redirect('home')
    else:
        form = ProfileForm(instance=request.user.profile)
    
    return render(request, 'users/edit_profile.html', {'form': form})

# Profilin silinməsi
@login_required
def delete_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        user = profile.user
        profile.delete()
        user.delete()  # İstifadəçini də silmək üçün
        messages.success(request, 'Profil və istifadəçi uğurla silindi.')
        return redirect('home')
    
    return render(request, 'users/delete_profile.html', {'profile': profile})


@login_required
def user_profile(request):
    profile = Profile.objects.get(user=request.user)
    context = {
        'profile': profile,
    }
    return render(request, 'users/user_profile.html', context)

def login_register(request):
    return render(request, 'users/login_register.html')



@login_required(login_url='login_register')
def home(request):
    salons = Salon.objects.all()
    barbers = Barber.objects.all()

    return render(request, 'users/home.html', {
        'salons': salons,
        'users': barbers,
    })

@login_required
def salon_detail(request, pk):
    salon = get_object_or_404(Salon, pk=pk)
    services = Services.objects.filter(salons=salon)
    barbers = Barber.objects.filter(salons=salon)
    return render(request, 'users/salon_detail.html', {
        'salon': salon,
        'services': services,
        'barbers': barbers,
    })


def barber_detail(request, pk):
    barber = get_object_or_404(Barber, pk=pk)
    services = Services.objects.filter(barbers=barber)
    salons = Salon.objects.filter(barbers=barber)
    return render(request, 'users/barber_detail.html', {
        'barber': barber,
        'services': services,
        'salons': salons,
    })


def login_register(request):
    return render(request, 'users/login_register.html')  

def register_choices(request):
    return render(request, 'users/register_choices.html')