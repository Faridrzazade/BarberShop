
from django.db.models.signals import m2m_changed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db import models


class SosialLinks(models.Model):
    tiktok_username = models.CharField(max_length=100)
    instagram_username = models.CharField(max_length=100)

    @property
    def tiktok_link(self):
        return f"https://www.tiktok.com/@{self.tiktok_username}"

    @property
    def instagram_link(self):  # Düzəliş edildi: instagram_username -> instagram_link
        return f"https://www.instagram.com/{self.instagram_username}"




class Barber(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/barber')
    description = models.TextField()
    services = models.ManyToManyField('services.BarberServices', related_name='barbers_list', blank=True)
    salons = models.ManyToManyField('salons.Salon', blank=True, related_name='barbers_in_salon')
    sosial_links = models.ForeignKey('users.SosialLinks', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


@receiver(m2m_changed, sender=Barber.salons.through)
def update_address(sender, instance, action, **kwargs):
    """
    Barber modelində salons sahəsi dəyişdirildikdə address sahəsini yeniləyir.
    """
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        if instance.salons.exists():
            instance.address = ', '.join(salon.address for salon in instance.salons.all())
        else:
            instance.address = ''  # Heç bir salon yoxdursa, address boş qoyulur.
        instance.save()



class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=16)
    phone = models.CharField(max_length=15)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Kişi'), ('female', 'Qadın'), ('other', 'Digər')], null=True, blank=True)

    def __str__(self):
        return self.user.name  # Düzəliş edildi: username -> name
