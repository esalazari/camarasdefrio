from decimal import Decimal
import logging
from django.conf import settings
from django.views.static import serve
import os
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from decouple import config
import openpyxl

## NEW
from email.message import EmailMessage
import smtplib

# APP's
from appCamara.models import Camara, Cotizacion, ValorTransporte
from appInicio.models import Region, Provincia, Comuna
from appDocumento.documentos.crear_cotizacion import crearCotizacion
from appDocumento.correos.envio_correo_cotizacion import enviarCorreoCotizacion
from appCliente.models import Cliente
from appUsuario.user_decorator import validarPermisosAutomatica


# Create your views here.
@validarPermisosAutomatica()
def inicio(request):
    _data = []
    _camaras = Camara.objects.filter(registroActivo=True)
    _regiones = Region.objects.filter(registroActivo=True)
    _comunas = Comuna.objects.filter(registroActivo=True)
    _valor_x_km = ValorTransporte.objects.filter(registroActivo=True, valor__isnull=False).latest('registroFechaCreacion')
    _correlativo = 0
    for _camara in _camaras:
        _correlativo += 1
        _neto = ('{:,.0f}'.format(_camara.valorNeto)).replace(',', '.')
        _iva = ('{:,.0f}'.format(_camara.valorIva)).replace(',', '.')
        _item = {
            'id': _camara.id,
            'correlativo': _correlativo,
            'nombre': _camara.nombre,
            'm2': str(_camara.m2).replace('.', ','),
            'm3': str(_camara.m3).replace('.', ','),
            'valorNeto': _neto,
            'valorIva': _iva,
            'ficha': str(_camara.ficha),
        }
        _data.append(_item)
            
    _context = {
        'camaras': _data,
        'regiones': _regiones,
        'comunas': _comunas,
        'valor_km': str(round(_valor_x_km.valor, 0)).replace(',', '.')
    }
    return render(request, "inicio.html", context=_context)

@validarPermisosAutomatica()
def listar_cotizaciones(request):
    _data = []
    _cotizaciones = Cotizacion.objects.filter(registroActivo=True)
    for _cotizacion in _cotizaciones:
        _item = {
            'id': _cotizacion.id,
            'correlativo': _cotizacion.correlativo,
            'fecha': _cotizacion.registroFechaCreacion,
            'neto': _cotizacion.neto,
            'iva': _cotizacion.iva,
            'total': _cotizacion.total,
        }
        _data.append(_item)
            
    _context = {
        'cotizacion': _data,
    }
    return render(request, "listar-cotizaciones.html", context=_context)


def pdf_view(request, url):
    file_path = os.path.join(settings.MEDIA_ROOT, url)
    with open(file_path, 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="{os.path.basename(file_path)}"'
        return response
        
def enviarCorreoCliente(request):
    _enviado = None
    _respuesta = 0
    _nombre_cliente = ''
    _observacion = ''
    _descuento = 0
    if request.method == 'POST':
        _correo = request.POST.get('correo-cliente')
        _selecionados = request.POST.get('numero-camara').split(',')
        _camaras = Camara.objects.filter(id__in=_selecionados)
        _checkbox = request.POST.get('check-datos-cliente')
        _check_observacion = request.POST.get('check-datos-observacion')
        _check_descuento = request.POST.get('check-datos-descuento')

        if _check_observacion == 'on':
            _observacion = request.POST.get('observacion')

        if _check_descuento == 'on':
            _descuento = request.POST.get('descuento')

        if _checkbox is None: # Cuando solo se debe enviar correo sin datos de cliente
            _enviado = enviarCorreoCotizacion(_correo, _camaras, _observacion, _descuento)
            _respuesta = 1
        else:
            _nombre = request.POST.get('nombre')
            _rut = request.POST.get('rut')
            _giro = request.POST.get('giro')
            _region = Region.objects.get(id=request.POST.get('region'))
            _comuna = Comuna.objects.get(id=request.POST.get('comuna'))
            _direccion = request.POST.get('direccion')
            _telefono = request.POST.get('telefono')
            _correo = request.POST.get('correo-cliente')
            try:
                _cliente = Cliente.objects.get(rut=_rut)
                _cliente.nombre = _nombre
                _cliente.giro = _giro
                _cliente.region = _region
                _cliente.comuna = _comuna
                _cliente.direccion = _direccion
                _cliente.telefono = _telefono
                _cliente.save()
                _respuesta = 2
            except Cliente.DoesNotExist:
                _cliente = Cliente.objects.create(nombre=_nombre, rut=_rut, giro=_giro, region=_region, comuna=_comuna, direccion=_direccion, telefono=_telefono, correo=_correo)
                _respuesta = 3  
            _nombre_cliente = _cliente.nombre
            _enviado = enviarCorreoCotizacion(_correo, _camaras, _observacion, _descuento, _cliente)
    json = { 'respuesta': _respuesta, 'cliente': _nombre_cliente, 'enviado': _enviado }
    return JsonResponse(json, safe=False)

def guardarCamaraFrio(request):
    _respuesta = False
    if request.method == 'POST':
        _nombre = request.POST.get('nombre')
        _m2 = request.POST.get('m2')
        _m3 = request.POST.get('m3')
        _valor = Decimal(request.POST.get('neto'))
        _iva = Decimal(_valor*Decimal(1.19))
        _ficha = request.FILES["guia"]
        try:
            _camara = Camara.objects.create(nombre=_nombre, m2=_m2, m3=_m3, valorNeto=_valor, valorIva=_iva, ficha=_ficha)
            _respuesta = True
        except:
            _respuesta = False
    json = { 'respuesta': _respuesta }
    return JsonResponse(json, safe=False)

def cambiarValorKm(request):
    _respuesta = False
    if request.method == 'POST':
        _valor = request.POST.get('valor')
        try:
            _nuevo = ValorTransporte.objects.create(valor=_valor)
            _respuesta = True
        except:
            _respuesta = False
    json = { 'respuesta': _respuesta, 'valor': _valor }
    return JsonResponse(json, safe=False)

def cambiarPrecioCamara(request):
    _respuesta = False
    _camaras = Camara.objects.filter(registroActivo=True)
    if request.method == 'POST':
        _valor = Decimal(request.POST.get('precio'))
        _porcentaje = Decimal(_valor/100)
        try:
            if _valor > 0:
                for _camara in _camaras:
                    _valor_neto = _camara.valorNeto + (_camara.valorNeto * _porcentaje)
                    _valor_iva = _valor_neto * (Decimal(1.19))
                    _camara.valorNeto = _valor_neto
                    _camara.valorIva = _valor_iva
                    _camara.save()
            elif _valor < 0:
                _porcentaje *= -1
                for _camara in _camaras:
                    _valor_neto = _camara.valorNeto - (_camara.valorNeto * _porcentaje)
                    _valor_iva = _valor_neto * (Decimal(1.19))
                    _camara.valorNeto = _valor_neto
                    _camara.valorIva = _valor_iva
                    _camara.save()
            _respuesta = True
        except:
            _respuesta = False
    json = { 'respuesta': _respuesta, 'valor': _valor }
    return JsonResponse(json, safe=False)


#FUNCIONES PARA CARGAR CONTACTOS
def cargarMasivaCamaras(request):
    _post = False
    _respuesta = True
    _registro_existentes = 0
    _registro_agregados = 0
    _registro_totales = 0
    if request.method == 'POST':        
        _documento = request.FILES.get('excel')
        _libro = openpyxl.load_workbook( _documento, data_only=True )
        #CARGA DE PROPUESTAS
        _hoja_activa = _libro['Sheet']
        _general = 0
        _total = 0
        _error = 0
        for _indice, _fila in enumerate( _hoja_activa.iter_rows( values_only = True ) ):
            if _indice > 0:
                try:
                    _nombre  = _fila[1]
                    _m2 = Decimal(_fila[2])
                    _m3 = Decimal(_fila[3])
                    _neto = Decimal(round(_fila[4]))
                    _iva = _neto * (Decimal(1.19))
                    
                    _item = {
                        'nombre' : _nombre,
                        'm2' : _m2,
                        'm3' : _m3,
                        'valorNeto' : _neto,
                        'valorIva': _iva
                    }
                    _camara = Camara.objects.filter(nombre = _nombre)

                    if not _camara:
                        _camara = Camara.objects.create(**_item)
                        _total += 1

                except Exception as e:
                    print(e)
                    logging.error('[CAMARA] ' + str(e) + ' ID->' + str(_fila[0]))
                    _error += 1
            _general += 1
            
        print('CAMARAS')
        print('GENERAL: ',_general)
        print('TOTAL: ',_total)
        print('ERROR: ',_error)

    _context = {
        'post' : _post,
        'existentes' : _registro_existentes,
        'agregados' : _registro_agregados,
        'no_agregados' : _registro_totales - _registro_agregados - _registro_existentes,
        'total' : _registro_totales,
        'respuesta' : _respuesta
    }
    return render(request, "cargar_camaras.html", context=_context)

def guardarFichaCamara(request):
    _respuesta = False
    print('funcion ficha')
    if request.method == 'POST':
        print('1')
        _camara = Camara.objects.get(id=request.POST.get('camara'))
        print(_camara)
        _ficha = request.FILES["ficha"]
        print(_ficha)
        print('2')

        try:
            _camara.ficha = _ficha
            _camara.save()
            _respuesta = True
        except:
            _respuesta = False
    json = { 'respuesta': _respuesta }
    return JsonResponse(json, safe=False)