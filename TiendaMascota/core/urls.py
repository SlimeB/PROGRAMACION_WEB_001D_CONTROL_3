from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import *
from django.contrib.auth.models import User
from .views_poblar_bd import *
from .views_comprar_produ import *
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', home, name="home"),
    path('poblar_bd', poblar_bd, name="poblar_bd"),
    path('producto_ficha_anon/<id>', producto_ficha, name="producto_ficha"),
    path('sobre_nosotros', sobre_nosotros, name="sobre_nosotros"),
    path('registrar/', registrar_usuario, name="registrar_usuario"),
    path('maestro_producto/<action>/<id>', maestro_producto, name="maestro_producto"),
    path('iniciar_sesion/', iniciar_sesion, name="iniciar_sesion"),
    path('mainAdministrador', mainAdministrador , name="mainAdministrador"),
    path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'),
    path('maestro_bodega/<action>/<id>', maestro_bodega, name="maestro_bodega"),
    path('inicio_cliente', inicio_cliente, name='inicio_cliente'),
    path('maestro_usuario/<action>/<id>', maestro_usuario, name="maestro_usuario"),
    path('mi_perfil', mi_perfil, name="mi_perfil"),
    path('comprar_producto/<id>', comprar_producto, name="comprar_producto"),
    path('registro_ventas', registro_ventas, name="registro_ventas"),
    path('detalle_factura/<id>', detalle_factura, name="detalle_factura"),
    path('mis_compras/<id>', mis_compras, name="mis_compras"),
    path('password_cambiada', TemplateView.as_view(template_name='core/password_cambiada.html'), name='password_cambiada'),
    path('cambiar_password', auth_views.PasswordChangeView.as_view(template_name='core/cambiar_password.html', success_url='/password_cambiada'), name='cambiar_password')
]