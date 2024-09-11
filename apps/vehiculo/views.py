from django.shortcuts import render


def vehiculo(request):
    return render(request, 'vehiculo/index.html')


def nuevos(request):
    return render(request, 'vehiculo/nuevos.html')

def usados(request):
    return render(request, 'vehiculo/usados.html')
