# Generated by Django 5.0.6 on 2024-10-31 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salons', '0011_rename_phone_number_salon_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='salon',
            name='password',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
    ]
