# Generated by Django 5.0.6 on 2024-10-31 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_barber_address_alter_barber_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='barber',
            name='password',
        ),
    ]
