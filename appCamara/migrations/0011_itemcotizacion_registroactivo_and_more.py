# Generated by Django 4.1.7 on 2023-05-19 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appCamara', '0010_cotizacion_totaldescuento'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemcotizacion',
            name='registroActivo',
            field=models.BooleanField(default=True, verbose_name='Registro Activo'),
        ),
        migrations.AddField(
            model_name='itemcotizacion',
            name='registroFechaCreacion',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de Creación'),
        ),
        migrations.AddField(
            model_name='itemcotizacion',
            name='registroFechaModificacion',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de\xa0Modificación'),
        ),
    ]
