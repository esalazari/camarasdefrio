import os
from django.conf import settings
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from appCamara.models import Cotizacion, ItemCotizacion

pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))
pdfmetrics.registerFont(TTFont('VeraIt', 'VeraIt.ttf'))
pdfmetrics.registerFont(TTFont('VeraBI', 'VeraBI.ttf'))

def descargarCotizacion(request, id_cot):
    cotizacion = Cotizacion.objects.get(id=id_cot)
    _items = ItemCotizacion.objects.filter(registroActivo=True, cotizacion=cotizacion)
    w, h = letter
    c = canvas.Canvas(r"media/cotizaciones/Cotizacion_camara.pdf", pagesize=letter)

    # LOGO MARCA DE AGUA
    c.drawImage("static/assets/img/cotizacion/fondo_agua.png", 0, h-500, width=600, height=200)

    # LOGO
    c.drawImage("static/assets/img/cotizacion/logo.png", 100, h-70, width=160, height=50)

    # TITULO
    c.setFillColorRGB(0.99609375, 0.26953125, 0)
    c.setFont('VeraBd', 16)
    c.drawString(75, h-95, 'AUTOMÁTICA INGENIERIA')

    # SUB TITULO
    c.setFillColorRGB(0, 0, 0)
    c.setFont('Vera', 9)
    c.drawString(45, h-105, 'INGENIERIA EN AUTOMATIZACIÓN Y REFRIGERACIÓN INDUSTRIAL')

    # DIRECCIÓN
    c.setFillColorRGB(0, 0, 0)
    c.setFont('Vera', 7)
    c.drawString(106, h-115, 'Del Consistorial # 6619, Cerro Navia, Santiago de Chile')

    # DIRECCIÓN WEB
    c.setFillColorRGB(0.99609375, 0.26953125, 0)
    c.setFont('VeraBd', 7)
    c.drawString(130, h-125, 'http://www.camarasdefrio.com')

    # RECTANGULO N°FACTURA
    c.setLineWidth(2)
    c.setStrokeColor('red')
    c.rect(380, h-110, 180, 85)

    # INFO DE RECTANGULO
    # RUT
    c.setFillColor('red')
    c.setFont('VeraBd', 10)
    c.drawString(425, h-50, 'R.U.T.77.000.639-2')
    # COTIZACIÓN
    c.setFillColor('red')
    c.setFont('VeraBd', 10)
    c.drawString(440, h-70, 'COTIZACIÓN')
    # NUMERO FACTURA
    c.setFillColor('red')
    c.setFont('VeraBd', 10)
    c.drawString(453, h-90, 'N° '+str(cotizacion.correlativo))

    # LOGO 2
    c.drawImage("static/assets/img/cotizacion/logo_camara_frio.png", 40, h-180, width=112, height=50)

    # LOGO 3
    c.drawImage("static/assets/img/cotizacion/logo_bandera.png", 170, h-165, width=25, height=18)

    # CORREO 1
    c.setFillColorRGB(0, 0, 0)
    c.setFont('Vera', 7)
    c.drawString(210, h-152, 'contacto@camarasdefrio.com')

    # CORREO 2
    c.setFillColorRGB(0, 0, 0)
    c.setFont('Vera', 7)
    c.drawString(210, h-162, 'robotech.ingeniería@gmail.com')

    # TELEFONO 1
    c.setFillColorRGB(0, 0, 0)
    c.setFont('Vera', 7)
    c.drawString(350, h-152, '+56942768657')

    # TELEFONO 2
    c.setFillColorRGB(0, 0, 0)
    c.setFont('Vera', 7)
    c.drawString(350, h-162, '+56987586070')

    # LOGO 4
    c.drawImage("static/assets/img/cotizacion/logo_sec.png", 420, h-176, width=70, height=45)

    # LOGO CAMARA CHILENA
    c.drawImage("static/assets/img/cotizacion/camara_chile.png", 495, h-166, width=80, height=25)

    # RECTANGULO DATOS CLIENTE
    c.setLineWidth(0.3)
    c.setStrokeColor('black')
    c.rect(20, h-270, 570, 75)

    # NOMBRE FORMULARIO
    c.setFillColor('black')
    c.setFont('VeraBd', 8)
    c.drawString(22, h-208, 'Señor(es): ')

    # NOMBRE DE CLIENTE
    c.setFillColorRGB(0, 0, 0)
    c.setFont('Vera', 8)
    c.drawString(75, h-208, str(cotizacion.sennor))

    # RUT FORMULARIO
    c.setFillColor('black')
    c.setFont('VeraBd', 8)
    c.drawString(22, h-220, 'R.U.T.: ')

    # RUT DE CLIENTE
    c.setFillColorRGB(0, 0, 0)
    c.setFont('Vera', 8)
    c.drawString(75, h-220, str(cotizacion.rut))

    # GIRO FORMULARIO
    c.setFillColor('black')
    c.setFont('VeraBd', 8)
    c.drawString(22, h-232, 'Giro: ')

    # GIRO DE CLIENTE
    c.setFillColorRGB(0, 0, 0)
    c.setFont('Vera', 8)
    c.drawString(75, h-232, str(cotizacion.giro))

    # DIRECCIÓN FORMULARIO
    c.setFillColor('black')
    c.setFont('VeraBd', 8)
    c.drawString(22, h-244, 'Dirección: ')

    # DIRECCIÓN DE CLIENTE
    c.setFillColorRGB(0, 0, 0)
    c.setFont('Vera', 8)
    c.drawString(75, h-244, str(cotizacion.direccion))

    # COMUNA FORMULARIO
    c.setFillColor('black')
    c.setFont('VeraBd', 8)
    c.drawString(22, h-256, 'Comuna: ')

    # COMUNA DE CLIENTE
    c.setFillColorRGB(0, 0, 0)
    c.setFont('Vera', 8)
    c.drawString(75, h-256, str(cotizacion.comuna))

    # CIUDAD FORMULARIO
    c.setFillColor('black')
    c.setFont('VeraBd', 8)
    c.drawString(22, h-268, 'Ciudad: ')

    # CIUDAD DE CLIENTE
    c.setFillColorRGB(0, 0, 0)
    c.setFont('Vera', 8)
    c.drawString(75, h-268, str(cotizacion.ciudad))

    # FECHA DE EMISIÓN FORMULARIO
    c.setFillColor('black')
    c.setFont('VeraBd', 8)
    c.drawString(355, h-208, 'Fecha Emisión: ')

    # FECHA DE EMISIÓN DE CLIENTE
    c.setFillColorRGB(0, 0, 0)
    c.setFont('Vera', 8)
    c.drawString(450, h-208, str(cotizacion.registroFechaCreacion.strftime("%d/%m/%Y")))

    # CONDICIÓN DE PAGO FORMULARIO
    c.setFillColor('black')
    c.setFont('VeraBd', 8)
    c.drawString(355, h-220, 'Condición de Pago: ')

    # CONDICIÓN DE PAGO DE CLIENTE
    c.setFillColorRGB(0, 0, 0)
    c.setFont('Vera', 8)
    c.drawString(450, h-220, 'CONTADO')

    # VENDEDOR FORMULARIO
    c.setFillColor('black')
    c.setFont('VeraBd', 8)
    c.drawString(355, h-232, 'Vendedor: ')

    # NOMBRE DE VENDEDOR
    c.setFillColorRGB(0, 0, 0)
    c.setFont('Vera', 8)
    c.drawString(450, h-232, 'MIGUEL SALAZAR')

    xlist = [20, 50, 100, 300, 350, 430, 510, 590]
    ylist = [h-270, h-283, h-600]

    c.setLineWidth(0.3)
    c.setStrokeColor('black')
    c.grid(xlist, ylist)

    # ITEM COLUMNA
    c.setFillColor('black')
    c.setFont('Vera', 8)
    c.drawString(22, h-280, '#Item')

    # CODIGO COLUMNA
    c.setFillColor('black')
    c.setFont('Vera', 8)
    c.drawString(52, h-280, 'Código')

    # DESCRIPCIÓN COLUMNA
    c.setFillColor('black')
    c.setFont('Vera', 8)
    c.drawString(102, h-280, 'Descripción')

    # CANTIDAD COLUMNA
    c.setFillColor('black')
    c.setFont('Vera', 8)
    c.drawString(302, h-280, 'Cantidad')

    # PRECIO UNIT. COLUMNA
    c.setFillColor('black')
    c.setFont('Vera', 8)
    c.drawString(352, h-280, 'Precio Unit.')

    # DESCUENTO COLUMNA
    c.setFillColor('black')
    c.setFont('Vera', 8)
    c.drawString(432, h-280, 'Descuento ($)')

    # VALOR COLUMNA
    c.setFillColor('black')
    c.setFont('Vera', 8)
    c.drawString(512, h-280, 'Valor')

    # RECTANGULO DE DATOS DE TRANSFERENCIA
    c.setLineWidth(0.1)
    c.setStrokeColor('black')
    c.rect(20, h-634, 570, 18)

    # INFORMACIÓN DE TRANSFERENCIA
    c.setFillColor('black')
    c.setFont('Vera', 8)
    c.drawString(22, h-628, 'DATOS DE TRANSFERENCIA: AUTOMATICA INGENIERIA RUT :77000639-2 BANCO ESTADO CHEQUERA ELECTRONICA 32170434985')

    # RECTANGULO DE OBSERVACIÓN
    c.setLineWidth(0.1)
    c.setStrokeColor('black')
    c.rect(20, h-720, 405, 70)

    # TITULO DE CUADRO PARA OBSERVACIÓN
    c.setFillColor('black')
    c.setFont('Vera', 8)
    c.drawString(23, h-660, 'Observación: ')

    # OBSERVACIÓN
    c.setFillColor('black')
    c.setFont('Vera', 8)
    c.drawString(23, h-670, str(cotizacion.observacion))

    # DATO DE CAMARA
    # descrpción de la camara
    _height = 295
    for _item in _items:
        c.setFillColor('black')
        c.setFont('Vera', 6)
        c.drawString(103, h-+_height, str(_item.descripcion))

        # cantidad de la camara
        c.setFillColor('black')
        c.setFont('Vera', 6)
        c.drawRightString(345, h-_height, '1')

        # precio unitario de la camara
        c.setFillColor('black')
        c.setFont('Vera', 6)
        c.drawRightString(425, h-_height, str('$ '+'{:,.0f}'.format(_item.precioUnitario)).replace(',', '.'))

        # precio valor de la camara
        c.setFillColor('black')
        c.setFont('Vera', 6)
        c.drawRightString(580, h-_height, str('$ '+'{:,.0f}'.format(_item.valor)).replace(',', '.'))
        _height += 10

    # RECTANGULO DE TOTALES
    c.setLineWidth(0.1)
    c.setStrokeColor('black')
    c.rect(445, h-720, 145, 70)

    # DESCUENTO DE CUADRO TOTALES
    c.setFillColor('black')
    c.setFont('VeraBd', 8)
    c.drawString(450, h-662, 'Sub Neto: ')

    # DATO DESCUENTO DE CUADRO TOTALES
    c.setFillColor('black')
    c.setFont('Vera', 8)
    c.drawRightString(584, h-662, str('$ '+'{:,.0f}'.format(cotizacion.subNeto)).replace(',', '.'))

    # EXENTO DE CUADRO TOTALES
    c.setFillColor('black')
    c.setFont('VeraBd', 8)
    c.drawString(450, h-674, 'Descuento: ('+str(round(cotizacion.descuento, 0))+'%)' )

    # DATO EXENTO DE CUADRO TOTALES
    c.setFillColor('black')
    c.setFont('Vera', 8)
    c.drawRightString(584, h-674, str('$ - '+'{:,.0f}'.format(cotizacion.totalDescuento if cotizacion.totalDescuento else 0)).replace(',', '.'))

    # NETO DE CUADRO TOTALES
    c.setFillColor('black')
    c.setFont('VeraBd', 8)
    c.drawString(450, h-686, 'NETO: ')

    # DATO NETO DE CUADRO TOTALES
    c.setFillColor('black')
    c.setFont('Vera', 8)
    c.drawRightString(584, h-686, '$ '+str('{:,.0f}'.format(cotizacion.neto)).replace(',', '.'))
    # c.drawString(570, h-686, '$ 0')

    # IVA DE CUADRO TOTALES
    c.setFillColor('black')
    c.setFont('VeraBd', 8)
    c.drawString(450, h-698, '19% I.V.A.: ')

    # DATO IVA DE CUADRO TOTALES
    c.setFillColor('black')
    c.setFont('Vera', 8)
    c.drawRightString(584, h-698, '$ '+str('{:,.0f}'.format(cotizacion.iva)).replace(',', '.'))
    # c.drawString(570, h-698, '$ 0')

    # TOTAL DE CUADRO TOTALES
    c.setFillColor('black')
    c.setFont('VeraBd', 8)
    c.drawString(450, h-710, 'TOTAL: ')

    # DATO TOTAL DE CUADRO TOTALES
    c.setFillColor('black')
    c.setFont('Vera', 8)
    c.drawRightString(584, h-710,'$ '+str('{:,.0f}'.format(cotizacion.total)).replace(',', '.'))
    # c.drawString(570, h-710, '$ 0')

    # MENSAJE DE LETRA CHICA
    c.setFillColor('black')
    c.setFont('Vera', 5)
    c.drawString(22, h-728, 'Cotización válida por 10 días desde la fecha que se realizó el documento, en caso de consultas, se debe contactar al número +569 42 76 8657, +569 87 58 6070 o al correo electrónico contacto@camarasdefrio.com')

    # LOGO KUKA
    c.drawImage("static/assets/img/cotizacion/logo_kuka.png", 20, h-778, width=70, height=15)

    # LOGO KUKA
    c.drawImage("static/assets/img/cotizacion/siemens_logo.png", 100, h-790, width=70, height=40)

    # LOGO BITZER
    c.drawImage("static/assets/img/cotizacion/bitzer_logo.png", 185, h-790, width=70, height=40)

    # LOGO DANFOSS
    c.drawImage("static/assets/img/cotizacion/danfoss_logo.png", 265, h-780, width=70, height=20)

    # LOGO ABB
    c.drawImage("static/assets/img/cotizacion/abb_logo.png", 340, h-780, width=70, height=20)

    # LOGO COPELAND
    c.drawImage("static/assets/img/cotizacion/copeland_logo.jpg", 420, h-780, width=70, height=20)

    # LOGO DORIN
    c.drawImage("static/assets/img/cotizacion/dorin_logo.png", 520, h-780, width=70, height=20)

    c.showPage()
    c.save()

    file_path = os.path.join(settings.MEDIA_ROOT, r"cotizaciones/Cotizacion_camara.pdf")
    with open(file_path, 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="cotización.pdf"'
        return response