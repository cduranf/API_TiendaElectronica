from django.db import models

""" class Perro( models.Model ):

    ESTADO = (
        ('Rescatado', 'Rescatado'),
        ('Disponible', 'Disponible'),
        ('Adoptado','Adoptado'),
    )   


    id = models.AutoField( primary_key = True )
    nombre = models.CharField( max_length = 255 )
    raza = models.TextField( default= '' )
    caracteristica = models.TextField( default= '' )
    estado = models.CharField( max_length = 255, default = 'disponible',choices= ESTADO )
    imageUrl = models.ImageField(upload_to='dog_image', blank=True)

    def __str__( self ):
        return self.nombre """

class Tienda( models.Model ):
    id = models.AutoField( primary_key = True )
    nom_tienda = models.CharField( max_length = 255 )
    direccion = models.CharField( max_length = 255 )
    ciudad = models.CharField( max_length = 255 )
    comuna = models.CharField( max_length = 255 )
    fono = models.CharField( max_length = 255 )
    correo_elect = models.CharField( max_length = 255 )
    encargado_local = models.CharField( max_length = 255)

    def __str__( self ):
        return self.nom_tienda

class Vendedor( models.Model ):
    id = models.AutoField( primary_key = True )
    nom_vendedor = models.CharField( max_length = 255 )
    #aca debe ir la dependecia de la tienda o por separa

    def __str__( self ):
        return self.nom_vendedor

class Producto( models.Model ):
    id = models.AutoField( primary_key = True )
    nom_producto = models.CharField( max_length = 255 )
    descripcion = models.CharField( max_length = 255 )
    precio = models.CharField( max_length = 255 )
    tipo_producto = models.CharField( max_length = 255 )

    def __str__( self ):
        return self.nom_vendedor



""" class User(models.Model):

    YES = '1'
    NO = '0'

    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    admin = models.CharField(max_length=10, default=NO) """