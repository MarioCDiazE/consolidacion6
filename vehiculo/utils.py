""" from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Vehiculo

def asignarPermiso(user):
    content_type = ContentType.objects.get_for_model(Vehiculo)
    visualuzarPermiso = Permission.objects.get(
        content_type=content_type,
        codename='visualizar_catalogo'
    )
    user.user_permissions.add(visualuzarPermiso)
    
    agregarPermiso = Permission.objects.get(
        content_type=content_type,
        codename='add_vehiculo'
    )
    user.user_permissions.add(agregarPermiso) """