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
    color = models.CharField(max_length=50, null=True, blank=True)
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


class FormularioDeBusqueda(models.Model):
    """
    Clase que representa un formulario de búsqueda, donde los usuarios pueden buscar 
    vehículos en función de criterios como marca, modelo, año, y precio.
    """

    nombre_completo = models.CharField(max_length=50)
    # Se puede agregar una validación adicional para números de teléfono
    numero = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año = models.IntegerField(null=True, blank=True)
    precio = models.DecimalField(
        null=True, blank=True, decimal_places=2, max_digits=10, validators=[MinValueValidator(0.00)]
    )

    def __str__(self):
        return f"{self.nombre_completo} - {self.marca} {self.modelo}"

    class Meta:
        verbose_name = "Formulario de Búsqueda"
        verbose_name_plural = "Formularios de Búsqueda"
