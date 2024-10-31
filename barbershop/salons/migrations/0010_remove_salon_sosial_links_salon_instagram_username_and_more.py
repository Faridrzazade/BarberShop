# Generated by Django 5.0.6 on 2024-10-31 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salons', '0009_remove_salon_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salon',
            name='sosial_links',
        ),
        migrations.AddField(
            model_name='salon',
            name='instagram_username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='salon',
            name='tiktok_username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]