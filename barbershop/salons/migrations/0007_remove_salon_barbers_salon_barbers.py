# Generated by Django 5.0.6 on 2024-10-30 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salons', '0006_alter_salon_services'),
        ('users', '0003_remove_barber_services_barber_services'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salon',
            name='barbers',
        ),
        migrations.AddField(
            model_name='salon',
            name='barbers',
            field=models.ManyToManyField(blank=True, related_name='salon_list', to='users.barber'),
        ),
    ]
