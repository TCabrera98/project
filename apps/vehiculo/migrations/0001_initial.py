# Generated by Django 5.1.1 on 2024-09-11 16:21

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormularioDeBusqueda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(max_length=50)),
                ('numero', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('año', models.IntegerField(blank=True, null=True)),
                ('precio', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0.0)])),
            ],
            options={
                'verbose_name': 'Formulario de Búsqueda',
                'verbose_name_plural': 'Formularios de Búsqueda',
            },
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('version', models.CharField(max_length=50)),
                ('año', models.IntegerField(blank=True, null=True)),
                ('kilometraje', models.IntegerField(default=0, null=True)),
                ('color', models.CharField(blank=True, max_length=50, null=True)),
                ('condicion', models.CharField(choices=[('0km', '0km'), ('Usado', 'Usado')], default='0km', max_length=50)),
            ],
            options={
                'verbose_name': 'Vehículo',
                'verbose_name_plural': 'Vehículos',
                'indexes': [models.Index(fields=['marca', 'modelo', 'año'], name='vehiculo_ve_marca_381dc2_idx')],
            },
        ),
        migrations.CreateModel(
            name='VehiculoImagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='vehiculo/imagenes/')),
                ('vehiculo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='vehiculo.vehiculo')),
            ],
        ),
    ]
