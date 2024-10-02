from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "vehiculo"

urlpatterns = [
    path('nuevos/', views.nuevos, name='nuevos'),
    path('usados/', views.usados, name='usados'),
    path('modal-imagenes/<int:vehiculo_id>/',
         views.modal_imagenes, name='modal_imagenes'),
    path('formulario_busqueda/', views.formulario_busqueda,
         name='formulario_busqueda'),
    path('formulario_enviado/', views.formulario_enviado,
         name='formulario_enviado'),

]

urlpatterns += staticfiles_urlpatterns()
