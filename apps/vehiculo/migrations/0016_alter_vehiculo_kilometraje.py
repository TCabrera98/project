# Generated by Django 5.1.1 on 2024-10-01 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0015_alter_vehiculo_kilometraje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='kilometraje',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
