from django.contrib.auth.hashers import make_password
from django.db.models.signals import m2m_changed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db import models
from salons.models import Salon




class Barber(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, blank=True)
    email = models.EmailField()
    address = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='media/barber')
    description = models.TextField()
    services = models.ManyToManyField('services.BarberServices', related_name='barbers_list', blank=True)
    salons = models.ManyToManyField('salons.Salon', blank=True, related_name='barbers_in_salon')
    
    # Sosial bağlantılar burada
    tiktok_username = models.CharField(max_length=100, blank=True, null=True)
    instagram_username = models.CharField(max_length=100, blank=True, null=True)

    password = models.CharField(max_length=128)  # Example of a password field

    def set_password(self, raw_password):
        self.password = make_password(raw_password) 

    @property
    def tiktok_link(self):
        if self.tiktok_username:
            return f"https://www.tiktok.com/@{self.tiktok_username}"
        return None

    @property
    def instagram_link(self):
        if self.instagram_username:
            return f"https://www.instagram.com/{self.instagram_username}"
        return None

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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    name = models.CharField(max_length=16)
    phone = models.CharField(max_length=15)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(
        max_length=10,
        choices=[
            ('male', 'Kişi'),
            ('female', 'Qadın'),
            ('other', 'Digər')
        ],
        null=True,
        blank=True
    )

    def __str__(self):
        return self.user.username
