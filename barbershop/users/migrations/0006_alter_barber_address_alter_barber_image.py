# Generated by Django 5.0.6 on 2024-10-31 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_barber_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barber',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='barber',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/barber'),
        ),
    ]
