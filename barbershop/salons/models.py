from django.db import models
from users.models import SosialLinks
# Bərbər salonlarının dataları. 


class Salon(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    description = models.TextField()
    barbers = models.ForeignKey('users.Barber', on_delete=models.SET_NULL, null=True, blank=True)
    services = models.ForeignKey('services.Services', on_delete=models.SET_NULL, null=True, blank=True, related_name='salons_list')
    image = models.ImageField(upload_to='media/salons')
    sosial_links = models.ForeignKey('users.SosialLinks', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name
