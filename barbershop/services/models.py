from django.db import models

# Bərbərin və salonun göstərdiyi xidmətlərin dataları.
class Services(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='media/services', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    salons = models.ForeignKey('salons.Salon', on_delete=models.SET_NULL, null=True, blank=True, related_name='services_list')
    barbers = models.ForeignKey('users.Barber', on_delete=models.SET_NULL, null=True, blank=True, related_name='services_list')

    def __str__(self):
        return self.name
