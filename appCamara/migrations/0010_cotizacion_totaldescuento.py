# Generated by Django 4.1.7 on 2023-05-18 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appCamara', '0009_remove_cotizacion_camara_remove_cotizacion_cliente_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cotizacion',
            name='totalDescuento',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=20, null=True, verbose_name='Total Descuento'),
        ),
    ]