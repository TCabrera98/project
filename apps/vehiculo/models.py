from django.db import models
from django.db import models
from django.core.validators import MinValueValidator

# Opciones para el campo "condición" del vehículo
CONDICION_VEHICULO = [
    ("0km", "0km"),
    ("Usado", "Usado"),
]


class Vehiculo(models.Model):
    """ 
    Clase que representa un vehículo con sus detalles principales, 
    como marca, modelo, versión, año, kilometraje y condición (0km o usado).
    """

    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    version = models.CharField(max_length=50)
    año = models.IntegerField(null=True, blank=True)
    kilometraje = models.IntegerField(null=True, default=0)
    condicion = models.CharField(
        max_length=50, choices=CONDICION_VEHICULO, default="0km")

    def __str__(self):
        return f"{self.marca} {self.modelo} {self.año}"

    class Meta:
        verbose_name = "Vehículo"
        verbose_name_plural = "Vehículos"
        indexes = [
            # Indexar campos usados para búsquedas frecuentes
            models.Index(fields=['marca', 'modelo', 'año']),
        ]


class VehiculoImagen(models.Model):
    """ 
    Clase para almacenar las imágenes asociadas a los vehículos. 
    Cada imagen está vinculada a un vehículo a través de una relación de ForeignKey.
    """

    vehiculo = models.ForeignKey(
        Vehiculo, related_name="imagenes", on_delete=models.CASCADE, null=True, blank=True
    )
    imagen = models.ImageField(upload_to="vehiculo/imagenes/")

    def __str__(self):
        return f"Imagen de {self.vehiculo}"

