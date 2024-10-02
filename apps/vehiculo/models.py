from django.db import models
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from datetime import datetime

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
    kilometraje = models.DecimalField(
        max_digits=15, decimal_places=0, null=True, default=0.0)
    condicion = models.CharField(
        max_length=50, choices=CONDICION_VEHICULO, default="0km")

    # Campos simplificados para la ficha técnica
    motor = models.CharField(max_length=20, null=True, blank=True)
    potencia = models.CharField(max_length=20, null=True, blank=True)
    transmision = models.CharField(max_length=50, null=True, blank=True)
    traccion = models.CharField(max_length=50, null=True, blank=True)
    tanque_combustible = models.CharField(max_length=20, null=True, blank=True)
    descripcion = models.TextField(
        null=True, blank=True, default="Sin información")

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


class ModeloFormularioBusqueda(models.Model):
    """
    Clase para crear un formulario de búsqueda de vehículos.
    """

    nombre_completo = models.CharField(max_length=100)
    numero_celular = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r"^\+?1?\d{9,15}$",
                message="Formato de número incorrecto. Intente nuevamente.",
            )
        ],
    )
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año_inicio = models.PositiveIntegerField(
        choices=[(año, año) for año in range(2008, datetime.now().year + 1)], null=True, blank=True, default="No especificado"
    )
    año_fin = models.PositiveIntegerField(
        choices=[(año, año) for año in range(2008, datetime.now().year + 1)], null=True, blank=True, default="No especificado"
    )

    def clean(self):
        # Obtiene el año actual
        año_actual = datetime.now().year

        # Verifica el año de inicio
        if self.año_inicio is not None and self.año_inicio > año_actual:
            raise ValidationError(
                f"El año de inicio no puede ser mayor a {año_actual}.")

        # Verifica el año de fin
        if self.año_fin is not None and self.año_fin > año_actual:
            raise ValidationError(
                f"El año de fin no puede ser mayor a {año_actual}.")

        # Verifica que el año de inicio no sea mayor al de fin
        if self.año_inicio is not None and self.año_fin is not None and self.año_inicio > self.año_fin:
            raise ValidationError(
                "El año de inicio no puede ser mayor al de fin.")

    def __str__(self):
        return f"{self.nombre_completo} {self.marca} {self.modelo} {self.año_inicio}-{self.año_fin}"
