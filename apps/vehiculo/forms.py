from django import forms
from .models import FormularioBusqueda


class FormularioBusquedaForm(forms.ModelForm):

    class Meta:
        model = FormularioBusqueda
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

        # Extra los valores del formulario
        nombre_completo = cleaned_data.get('nombre_completo')
        marca = cleaned_data.get('marca')
        modelo = cleaned_data.get('modelo')
        año_inicio = cleaned_data.get('año_inicio')
        año_fin = cleaned_data.get('año_fin')
        numero_celular = cleaned_data.get("numero_celular")

        # Normaliza los datos
        if nombre_completo:
            cleaned_data['nombre_completo'] = nombre_completo.upper()
        if marca:
            # Strip para eliminar espacios en blanco
            cleaned_data['marca'] = marca.strip().capitalize()
        if modelo:
            cleaned_data['modelo'] = modelo.strip().capitalize()

        # Validación de años
        if año_inicio is not None and año_fin is not None:
            if año_inicio > año_fin:
                self.add_error(
                    'año_inicio', 'El año de inicio no puede ser mayor al año de fin.')
                self.add_error(
                    'año_fin', 'Debe ser igual o posterior al año de inicio.')

             # Validación de número de celular
            if numero_celular:
                if not numero_celular.isnumeric():
                    self.add_error('numero_celular',
                                   'El número de celular debe ser numérico.')

        return cleaned_data
