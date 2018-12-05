""" from .models import Perro """
from .models import Tienda
from .models import Vendedor
from .models import Producto
from rest_framework import viewsets
""" from misPerris.serializers import PerroSerializer """
from misPerris.serializers import TiendaSerializer
from misPerris.serializers import VendedorSerializer
from misPerris.serializers import ProductoSerializer

""" class PerroViewSet( viewsets.ModelViewSet ):
    queryset = Perro.objects.all().order_by( 'nombre' )
    serializer_class = PerroSerializer """



class TiendaViewSet (viewsets.ModelViewSet ):
    queryset = Tienda.objects.all().order_by( 'nom_tienda' )
    serializer_class = TiendaSerializer


class VendedorViewSet ( viewsets.ModelViewSet ):
    queryset = Vendedor.objects.all().order_by( 'nom_vendedor' )
    serializer_class = VendedorSerializer


class ProductoViewSet ( viewsets.ModelViewSet ):
    queryset = Producto.objects.all().order_by( 'nom_producto' )
    serializer_class = ProductoSerializer