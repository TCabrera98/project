from django.shortcuts import render


def vehiculo(request):
    return render(request, 'vehiculo/index.html')
