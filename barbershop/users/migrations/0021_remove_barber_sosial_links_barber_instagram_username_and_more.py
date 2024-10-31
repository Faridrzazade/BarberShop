# Generated by Django 5.0.6 on 2024-10-31 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salons', '0010_remove_salon_sosial_links_salon_instagram_username_and_more'),
        ('users', '0020_alter_barber_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='barber',
            name='sosial_links',
        ),
        migrations.AddField(
            model_name='barber',
            name='instagram_username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='barber',
            name='tiktok_username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='SosialLinks',
        ),
    ]
