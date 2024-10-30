from django.db import models
from django.contrib.auth.models import User


class SosialLinks(models.Model):
    tiktok_username = models.CharField(max_length=100)
    instagram_username = models.CharField(max_length=100)

    @property
    def tiktok_link(self):
        return f"https://www.tiktok.com/@{self.tiktok_username}"

    @property
    def instagram_link(self):  # Düzəliş edildi: instagram_username -> instagram_link
        return f"https://www.instagram.com/{self.instagram_username}"




# İstifadəçi dataları Bərbər qismində. 
class Barber(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/barber')
    description = models.TextField()
    services = models.ForeignKey('services.Services', on_delete=models.SET_NULL, null=True, blank=True, related_name='barbers_list')
    salons = models.ForeignKey('salons.Salon', on_delete=models.SET_NULL, blank=True, null=True, related_name='barbers_list')
    sosial_links = models.ForeignKey('users.SosialLinks', on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.salons:
            self.address = self.salons.address
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=16)
    phone = models.CharField(max_length=15)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Kişi'), ('female', 'Qadın'), ('other', 'Digər')], null=True, blank=True)

    def __str__(self):
        return self.user.name  # Düzəliş edildi: username -> name
