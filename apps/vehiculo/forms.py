from django import forms
from .models import ModeloFormularioBusqueda


class ModeloFormularioBusquedaForm(forms.ModelForm):

    class Meta:
        model = ModeloFormularioBusqueda
        fields = [
            'nombre_completo',
            'numero_celular',
            'marca',
            'modelo',
            'año_inicio',
            'año_fin',
        ]

        widgets = {
            'nombre_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_celular': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.Select(attrs={'class': 'form-control'}),
            'modelo': forms.Select(attrs={'class': 'form-control'}),
            'año_inicio': forms.Select(attrs={'class': 'form-control'}),
            'año_fin': forms.Select(attrs={'class': 'form-control'}),
        }

        labels = {
            'nombre_completo': 'Nombre completo',
            'numero_celular': 'Número de celular',
            'marca': 'Marca',
            'modelo': 'Modelo',
            'año_inicio': 'Año',
            'año_fin': 'Año',
        }

    def clean(self):
        cleaned_data = super().clean()
        nombre_completo = cleaned_data.get('nombre_completo')
        marca = cleaned_data.get('marca')
        modelo = cleaned_data.get('modelo')

        if nombre_completo:
            cleaned_data['nombre_completo'] = nombre_completo.upper()
        if marca:
            cleaned_data['marca'] = marca.capitalize()
        if modelo:
            cleaned_data['modelo'] = modelo.capitalize()
        return cleaned_data
