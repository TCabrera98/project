# Generated by Django 5.1.1 on 2024-09-26 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0004_vehiculo_consumo_promedio_vehiculo_potencia_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='cilindrada',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
