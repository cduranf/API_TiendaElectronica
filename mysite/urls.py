from django.contrib import admin
from django.urls import path
from rest_framework import routers
""" from misPerris.models import Perro """
from misPerris.models import Tienda
from misPerris.models import Vendedor
from misPerris.models import Producto
from misPerris import views
from django.conf.urls import url, include

router = routers.DefaultRouter()
""" router.register( r'perros', views.PerroViewSet ) """
router.register( r'tiendas', views.TiendaViewSet )
router.register( r'vendedores', views.VendedorViewSet )
router.register( r'productos', views.ProductoViewSet )


urlpatterns = [
    path( 'admin/', admin.site.urls ),
    url( r'^', include( router.urls ) ),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
