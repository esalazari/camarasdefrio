from django.db import models
from django.contrib.auth.models import User
from appCliente.models import Cliente

# Create your models here.

class TipoCamara(models.Model):
    descripcion = models.CharField(max_length=255, null = True, blank = True, default = None, verbose_name = 'Descripcion')
    ### Datos de Log ###
    registroActivo = models.BooleanField( default = True, verbose_name = 'Registro Activo' )
    registroFechaCreacion = models.DateTimeField( null=False, blank=False, auto_now_add=True, verbose_name = 'Fecha de Creación')
    registroFechaModificacion = models.DateTimeField( null=False, blank=False, auto_now=True, verbose_name = 'Fecha de Modificación')

    class Meta:
        ordering = ['descripcion']
        verbose_name = 'Tipo De Camara'
        verbose_name_plural = 'Tipos de Camaras'

    def __str__(self):
        return self.descripcion

class Camara(models.Model):
    nombre = models.CharField( null = True, blank = True, max_length=100, default = None, verbose_name = 'Nombre')
    tipo = models.ForeignKey(TipoCamara, on_delete = models.CASCADE, null = True, blank = True, default = None, verbose_name = 'Tipo de Camara')
    descripcion = models.CharField(max_length=255, null = True, blank = True, default = None, verbose_name = 'Descripcion')
    m2 = models.DecimalField(max_digits=20, decimal_places=2, null = True, blank = True, default = None, verbose_name = 'Metros Cuadrados')
    m3 = models.DecimalField(max_digits=20, decimal_places=2, null = True, blank = True, default = None, verbose_name = 'Metros Cubicos')
    uf = models.DecimalField(max_digits=20, decimal_places=2, null = True, blank = True, default = None, verbose_name = 'UF')
    valorNeto = models.DecimalField(max_digits=20, decimal_places=2, null = True, blank = True, default = None, verbose_name = 'Valor Neto')
    valorIva = models.DecimalField(max_digits=20, decimal_places=2, null = True, blank = True, default = None, verbose_name = 'Valor IVA')
    ficha = models.FileField(upload_to ='guias/camaras/', null = True, blank = True, default = None, verbose_name = 'Ficha')
    ### Datos de Log ###
    registroActivo = models.BooleanField( default = True, verbose_name = 'Registro Activo' )
    registroFechaCreacion = models.DateTimeField( null=False, blank=False, auto_now_add=True, verbose_name = 'Fecha de Creación')
    registroFechaModificacion = models.DateTimeField( null=False, blank=False, auto_now=True, verbose_name = 'Fecha de Modificación')

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Camara'
        verbose_name_plural = 'Camaras'

    def __str__(self):
        return str(self.nombre)
    
class TipoPago(models.Model):
    descripcion = models.CharField(max_length=255, null = True, blank = True, default = None, verbose_name = 'Descripcion')
    ### Datos de Log ###
    registroActivo = models.BooleanField( default = True, verbose_name = 'Registro Activo' )
    registroFechaCreacion = models.DateTimeField( null=False, blank=False, auto_now_add=True, verbose_name = 'Fecha de Creación')
    registroFechaModificacion = models.DateTimeField( null=False, blank=False, auto_now=True, verbose_name = 'Fecha de Modificación')

    class Meta:
        ordering = ['descripcion']
        verbose_name = 'Tipo De Pago'
        verbose_name_plural = 'Tipos de Pagos'

    def __str__(self):
        return str(self.descripcion)
    
class Cotizacion(models.Model):
    # Número de Factura
    correlativo = models.IntegerField(default=None, null=True, blank=True, verbose_name="Correlativo")
    # Información de Cliente
    sennor = models.CharField(max_length=250, null=True, blank=True, default=None, verbose_name='Señor')
    rut = models.CharField(max_length=250, null=True, blank=True, default=None, verbose_name='RUT')
    giro = models.CharField(max_length=250, null=True, blank=True, default=None, verbose_name='Giro Comercial')
    direccion = models.CharField(max_length=250, null=True, blank=True, default=None, verbose_name='Dirección')
    comuna = models.CharField(max_length=250, null=True, blank=True, default=None, verbose_name='Comuna')
    ciudad = models.CharField(max_length=250, null=True, blank=True, default=None, verbose_name='Ciudad')
    tipo = models.CharField(max_length=250, null=True, blank=True, default=None, verbose_name='Condición de Pago')
    vendedor = models.CharField(max_length=250, null=True, blank=True, default=None, verbose_name='Vendedor')
    # Totales
    observacion = models.CharField(max_length=250, null=True, blank=True, default=None, verbose_name='Observación')
    descuento = models.DecimalField(max_digits=20, decimal_places=2, null = True, blank = True, default = None, verbose_name = 'Descuento')
    totalDescuento = models.DecimalField(max_digits=20, decimal_places=2, null = True, blank = True, default = None, verbose_name = 'Total Descuento')
    subNeto = models.DecimalField(max_digits=20, decimal_places=2, null = True, blank = True, default = None, verbose_name = 'Valor SubNeto')
    neto = models.DecimalField(max_digits=20, decimal_places=2, null = True, blank = True, default = None, verbose_name = 'Valor Neto')
    iva = models.DecimalField(max_digits=20, decimal_places=2, null = True, blank = True, default = None, verbose_name = 'Valor IVA')
    total = models.DecimalField(max_digits=20, decimal_places=2, null = True, blank = True, default = None, verbose_name = 'Valor Total')
    intalacion = models.DecimalField(max_digits=20, decimal_places=2, null = True, blank = True, default = None, verbose_name = 'Valor Intalación')
    transporte = models.DecimalField(max_digits=20, decimal_places=2, null = True, blank = True, default = None, verbose_name = 'Valor Transporte')
    ### Datos de Log ###
    registroActivo = models.BooleanField( default = True, verbose_name = 'Registro Activo' )
    registroFechaCreacion = models.DateTimeField( null=False, blank=False, auto_now_add=True, verbose_name = 'Fecha de Creación')
    registroFechaModificacion = models.DateTimeField( null=False, blank=False, auto_now=True, verbose_name = 'Fecha de Modificación')

    class Meta:
        ordering = ['correlativo']
        verbose_name = 'Cotización'
        verbose_name_plural = 'Cotizaciones'

    def __str__(self):
        return str(self.correlativo)
    
class ValorTransporte(models.Model):
    valor = models.DecimalField(max_digits=20, decimal_places=2, null = True, blank = True, default = None, verbose_name = 'Valor x KM')
    ### Datos de Log ###
    registroActivo = models.BooleanField( default = True, verbose_name = 'Registro Activo' )
    registroFechaCreacion = models.DateTimeField( null=False, blank=False, auto_now_add=True, verbose_name = 'Fecha de Creación')
    registroFechaModificacion = models.DateTimeField( null=False, blank=False, auto_now=True, verbose_name = 'Fecha de Modificación')

    class Meta:
        ordering = ['valor']
        verbose_name = 'Valor KM'
        verbose_name_plural = 'Valores KMs'

    def __str__(self):
        return str(self.valor)
    
class ItemCotizacion(models.Model):
    cotizacion = models.ForeignKey(Cotizacion, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Cotización')
    item = models.CharField(max_length=255, null = True, blank = True, default = None, verbose_name = 'Item')
    codigo = models.CharField(max_length=255, null = True, blank = True, default = None, verbose_name = 'Código')
    descripcion = models.CharField(max_length=255, null = True, blank = True, default = None, verbose_name = 'Descripcion')
    cantidad = models.DecimalField(max_digits=20, decimal_places=2, null = True, blank = True, default = None, verbose_name = 'Cantidad')
    precioUnitario = models.DecimalField(max_digits=20, decimal_places=2, null = True, blank = True, default = None, verbose_name = 'Precio Unitario')
    descuento = models.DecimalField(max_digits=20, decimal_places=2, null = True, blank = True, default = None, verbose_name = 'Descuento')
    valor = models.DecimalField(max_digits=20, decimal_places=2, null = True, blank = True, default = None, verbose_name = 'Valor')
    ### Datos de Log ###
    registroActivo = models.BooleanField( default = True, verbose_name = 'Registro Activo' )
    registroFechaCreacion = models.DateTimeField( null=True, blank=True, auto_now_add=True, verbose_name = 'Fecha de Creación')
    registroFechaModificacion = models.DateTimeField( null=True, blank=True, auto_now=True, verbose_name = 'Fecha de Modificación')
    class Meta:
        ordering = ['id']
        verbose_name = 'Item de Cotización'
        verbose_name_plural = 'Items de la Cotización'

    def __str__(self):
        return str(self.id)
