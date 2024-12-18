from django.db import models
from django.contrib.auth.models import Permission

# Create your models here.

class Vehiculo(models.Model): 
    MARCAS = [
        ( 'FIAT', 'Fiat'),
        ( 'TOYOTA', 'Toyota'),
        ('FORD', 'Ford'),
        ('CHEVROLET', 'Chevrolet')
    ]
    CATEGORIAS = [
        ('PARTICULAR', 'Particular'),
        ('TRANSPORTE', 'Transporte'),
        ('CARGA', 'Carga')
    ]
    marca = models.CharField(max_length=20, choices=MARCAS, default='Ford')
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='Particular')
    precio = models.FloatField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = [
            ('visualizar_catalogo', 'Tienes permiso para visualizar el catalogo de vehiculos'),
            ('puede_agregar_vehiculo', 'Puedes agregar un vehiculo al catalogo'),
        ]

    def condicion_precio(self):
        if self.precio <= 10000:
            return 'Bajo'
        elif 10000 < self.precio <= 30000:
            return 'Medio'
        else:
            return 'Alto'

    def __str__(self):
        return f'{self.marca} {self.modelo} {self.serial_carroceria} {self.serial_motor} {self.categoria} {self.precio} {self.fecha_creacion} {self.fecha_modificacion}'

""" def get_permissions():
    permission, created = Permission.objects.get_or_create(
        codename='visualizar_catalogo',
        name='tienes permiso para visualizar el catalogo de vehiculos',
    )
    return permission """