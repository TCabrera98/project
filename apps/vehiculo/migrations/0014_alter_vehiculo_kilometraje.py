# Generated by Django 5.1.1 on 2024-09-30 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0013_alter_modeloformulariobusqueda_año_fin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='kilometraje',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=15, null=True),
        ),
    ]
