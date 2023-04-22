from django.urls import path
from appCamara import dx, views

urlpatterns = [
    # VIEWS 
    path('listar-camaras', views.listar_camaras, name='listar-camaras'),
    # DX
    path('inicio-listar-camaras', dx.jsonListarCamaras, name='inicio-listar-camaras'),

]