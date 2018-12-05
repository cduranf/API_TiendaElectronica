""" from .models import Perro
from .models import User """
from .models import Tienda
from .models import Vendedor
from .models import Producto
from rest_framework import serializers

""" 
class PerroSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Perro
        fields = ( 'id','nombre', 'raza', 'caracteristica', 'estado', 'imageUrl' )



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username','password', 'admin') """


class TiendaSerializer ( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Tienda
        fields = ( 'id', 'nom_tienda', 'direccion', 'ciudad', 'comuna', 'fono', 'correo_elect','encargado_local' )


class VendedorSerializer ( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Vendedor
        fields = ( 'id', 'nom_vendedor' )


class ProductoSerializer ( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Producto
        fields = ( 'id', 'nom_producto', 'descripcion', 'precio', 'tipo_producto' )