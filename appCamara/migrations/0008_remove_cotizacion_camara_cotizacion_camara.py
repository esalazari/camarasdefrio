# Generated by Django 4.1.7 on 2023-05-15 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appCamara', '0007_valortransporte'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cotizacion',
            name='camara',
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='camara',
            field=models.ManyToManyField(blank=True, to='appCamara.camara', verbose_name='Cámaras'),
        ),
    ]
