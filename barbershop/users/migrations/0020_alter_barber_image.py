# Generated by Django 5.0.6 on 2024-10-31 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_alter_barber_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barber',
            name='image',
            field=models.ImageField(default=1, upload_to='media/barber'),
            preserve_default=False,
        ),
    ]
