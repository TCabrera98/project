from django.shortcuts import render


def home(request):
    return render(request, 'home/base.html')


def nosotros(request):
    return render(request, "home/nosotros.html")
