# Generated by Django 5.0.6 on 2024-10-31 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salons', '0007_remove_salon_barbers_salon_barbers'),
    ]

    operations = [
        migrations.AddField(
            model_name='salon',
            name='password',
            field=models.CharField(default=1, max_length=32),
            preserve_default=False,
        ),
    ]