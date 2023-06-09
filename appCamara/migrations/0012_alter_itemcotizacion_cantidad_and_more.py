# Generated by Django 4.1.7 on 2023-05-19 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appCamara', '0011_itemcotizacion_registroactivo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemcotizacion',
            name='cantidad',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=20, null=True, verbose_name='Cantidad'),
        ),
        migrations.AlterField(
            model_name='itemcotizacion',
            name='descuento',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=20, null=True, verbose_name='Descuento'),
        ),
        migrations.AlterField(
            model_name='itemcotizacion',
            name='precioUnitario',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=20, null=True, verbose_name='Precio Unitario'),
        ),
        migrations.AlterField(
            model_name='itemcotizacion',
            name='valor',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=20, null=True, verbose_name='Valor'),
        ),
    ]
