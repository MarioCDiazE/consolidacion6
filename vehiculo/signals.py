from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from .models import Vehiculo
from django.contrib.contenttypes.models import ContentType

@receiver(post_save, sender=User)
def assign_permissions(sender, instance,created, **kwargs):
    if created:
        content_type = ContentType.objects.get_for_model(Vehiculo)
        visualizarPermiso = Permission.objects.get(
            content_type=content_type,
            codename='visualizar_catalogo'
        )
        instance.user_permissions.add(visualizarPermiso)
        agregarPermiso = Permission.objects.get(
            content_type=content_type,
            codename='add_vehiculo'
        )
        instance.user_permissions.add(agregarPermiso)