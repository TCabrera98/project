# Generated by Django 5.1.1 on 2024-09-16 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0002_delete_formulariodebusqueda'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehiculo',
            name='color',
        ),
    ]
