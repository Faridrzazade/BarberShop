# Generated by Django 5.0.6 on 2024-10-30 23:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salons', '0003_alter_salon_image'),
        ('services', '0002_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='barbers',
        ),
        migrations.RemoveField(
            model_name='services',
            name='salons',
        ),
        migrations.CreateModel(
            name='BarberServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=5, max_digits=10)),
                ('price_curency', models.CharField(max_length=2)),
                ('barber', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.barber')),
            ],
        ),
        migrations.CreateModel(
            name='SalonServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=5, max_digits=10)),
                ('price_curency', models.CharField(max_length=2)),
                ('salons', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='services_list', to='salons.salon')),
            ],
        ),
    ]
