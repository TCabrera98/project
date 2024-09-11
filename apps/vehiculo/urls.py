from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "vehiculo"

urlpatterns = [
    path('', views.vehiculo, name='vehiculo'),
    path('nuevos/', views.nuevos, name='nuevos'),
    path('usados/', views.usados, name='usados'),
]

urlpatterns += staticfiles_urlpatterns()
