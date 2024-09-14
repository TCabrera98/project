from django.shortcuts import render, get_object_or_404
from vehiculo.models import Vehiculo


def vehiculo(request):
    return render(request, 'vehiculo/index.html')


def nuevos(request):
    marca = request.GET.get("marca", "")
    modelo = request.GET.get("modelo", "")

    # Obtiene todas las marcas de los vehículos 0km
    marcas = Vehiculo.objects.filter(condicion="0km").values_list(
        "marca", flat=True).distinct()
    vehiculos_nuevos = Vehiculo.objects.filter(condicion="0km")

    # Filtra los vehículos por marca y modelo
    if marca:
        vehiculos_nuevos = vehiculos_nuevos.filter(marca__icontains=marca)
        modelos = Vehiculo.objects.filter(marca__icontains=marca).values_list(
            "modelo", flat=True).distinct()
    else:
        modelos = Vehiculo.objects.none()

    if modelo:
        vehiculos_nuevos = vehiculos_nuevos.filter(modelo__icontains=modelo)

    contexto = {
        "marcas": marcas,
        "vehiculos": vehiculos_nuevos,
        "marca": marca,
        "modelo": modelo,
        "modelos": modelos
    }
    return render(request, "vehiculo/nuevos.html", contexto)


def usados(request):
    marca = request.GET.get("marca", "")
    modelo = request.GET.get("modelo", "")

    # Obtiene todas las marcas de los vehículos usados
    marcas = Vehiculo.objects.filter(condicion="Usado").values_list(
        "marca", flat=True).distinct()
    vehiculos_usados = Vehiculo.objects.filter(condicion="Usado")

    # Filtra los vehículos por marca y modelo
    if marca:
        vehiculos_usados = vehiculos_usados.filter(marca__icontains=marca)
        modelos = Vehiculo.objects.filter(marca__icontains=marca).values_list(
            "modelo", flat=True).distinct()
    else:
        modelos = Vehiculo.objects.none()

    if modelo:
        vehiculos_usados = vehiculos_usados.filter(modelo__icontains=modelo)

    contexto = {
        "marcas": marcas,
        "vehiculos": vehiculos_usados,
        "marca": marca,
        "modelo": modelo,
        "modelos": modelos
    }
    return render(request, "vehiculo/usados.html", contexto)


def modal_imagenes(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    contexto = {
        "vehiculo": vehiculo
    }
    return render(request, "vehiculo/modal_imagenes.html", contexto)
