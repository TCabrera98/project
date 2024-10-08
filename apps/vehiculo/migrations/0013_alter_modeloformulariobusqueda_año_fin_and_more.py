# Generated by Django 5.1.1 on 2024-09-30 22:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0012_modeloformulariobusqueda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modeloformulariobusqueda',
            name='año_fin',
            field=models.PositiveIntegerField(blank=True, choices=[(2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024)], default='No especificado', null=True),
        ),
        migrations.AlterField(
            model_name='modeloformulariobusqueda',
            name='año_inicio',
            field=models.PositiveIntegerField(blank=True, choices=[(2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024)], default='No especificado', null=True),
        ),
        migrations.AlterField(
            model_name='modeloformulariobusqueda',
            name='numero_celular',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='Formato de número incorrecto. Intente nuevamente.', regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='kilometraje',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=15, null=True),
        ),
    ]
