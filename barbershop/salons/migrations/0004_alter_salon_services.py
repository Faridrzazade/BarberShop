# Generated by Django 5.0.6 on 2024-10-30 23:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salons', '0003_alter_salon_image'),
        ('services', '0003_remove_services_barbers_remove_services_salons_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salon',
            name='services',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='salons_list', to='services.salonservices'),
        ),
    ]
