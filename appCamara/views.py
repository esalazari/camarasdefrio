from urllib import request
from django.shortcuts import render
from appCamara.models import Camara
from appInicio.models import Region, Comuna

# Create your views here.

def listar_camaras(request):
    _data = []
    _correlativo = 0
    _camaras = Camara.objects.filter(registroActivo=True)
    _regiones = Region.objects.filter(registroActivo=True)
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
    }
    return render(request, "listar-camaras.html", context=_context)
