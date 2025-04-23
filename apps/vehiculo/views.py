from django.shortcuts import render, redirect, get_object_or_404
from vehiculo.models import Vehiculo
from django.contrib import messages
from vehiculo.forms import ModeloFormularioBusquedaForm


def nuevos(request):
    marca = request.GET.get("marca", "")
    modelo = request.GET.get("modelo", "")

    # Obtiene todas las marcas de los vehículos 0km
    marcas = Vehiculo.objects.filter(condicion="0km").values_list(
        "marca", flat=True).distinct()
    vehiculos_nuevos = Vehiculo.objects.filter(
        condicion="0km").order_by("-id")

    # Filtra los vehículos por marca y modelo
    if marca:
        vehiculos_nuevos = vehiculos_nuevos.filter(marca__icontains=marca)
        modelos = Vehiculo.objects.filter(condicion="0km", marca__icontains=marca).values_list(
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
        "modelos": modelos,
    }
    return render(request, "vehiculo/nuevos.html", contexto)


def usados(request):
    marca = request.GET.get("marca", "")
    modelo = request.GET.get("modelo", "")

    # Obtiene todas las marcas de los vehículos usados
    marcas = Vehiculo.objects.filter(condicion="Usado").values_list(
        "marca", flat=True).distinct()
    vehiculos_usados = Vehiculo.objects.filter(
        condicion="Usado").order_by("-id")

    # Filtra los vehículos por marca y modelo
    if marca:
        vehiculos_usados = vehiculos_usados.filter(
            condicion="Usado", marca__icontains=marca)
        modelos = Vehiculo.objects.filter(condicion="Usado", marca__icontains=marca).values_list(
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


def comparar_vehiculos(request):
    vehiculo_id_1 = request.GET.get("vehiculo_1")
    vehiculo_id_2 = request.GET.get("vehiculo_2")

    # Mensaje de error si no selecciona ningun vehiculo
    if not vehiculo_id_1 and not vehiculo_id_2:
        messages.warning(
            request, "Debe seleccionar para comparar.")
        return redirect("vehiculo:formulario_comparar")

    # Mensaje de error si solo selecciona un vehiculo
    if not vehiculo_id_1 or not vehiculo_id_2:
        messages.warning(
            request, "Debe seleccionar ambos vehiculos para comparar.")
        return redirect("vehiculo:formulario_comparar")

    # Mensaje de error si selecciona el mismo vehiculo
    if vehiculo_id_1 == vehiculo_id_2:
        messages.warning(request, "No se compararán dos vehiculos iguales.")
        return redirect("vehiculo:formulario_comparar")

    vehiculo1 = get_object_or_404(Vehiculo, id=vehiculo_id_1)
    vehiculo2 = get_object_or_404(Vehiculo, id=vehiculo_id_2)

    contexto = {
        "vehiculo1": vehiculo1,
        "vehiculo2": vehiculo2,
    }

    return render(request, "vehiculo/comparar_vehiculos.html", contexto)


def formulario_comparar(request):
    # Obtén todos los vehículos de la base de datos
    vehiculos = Vehiculo.objects.all()
    return render(request, 'vehiculo/formulario_comparar.html', {'vehiculos': vehiculos})


def modal_imagenes(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    contexto = {
        "vehiculo": vehiculo
    }
    return render(request, "vehiculo/modal_imagenes.html", contexto)


def formulario_busqueda(request):
    form = ModeloFormularioBusquedaForm()
    if request.method == "POST":
        form = ModeloFormularioBusquedaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("vehiculo:formulario_enviado")
    contexto = {
        "form": form
    }
    return render(request, "vehiculo/formulario_busqueda.html", contexto)


def formulario_enviado(request):
    return render(request, "vehiculo/formulario_enviado.html")
