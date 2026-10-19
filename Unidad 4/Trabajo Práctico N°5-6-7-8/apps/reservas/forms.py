from django import forms
from .models import ActividadDeportiva

class ActividadDeportivaForm(forms.ModelForm):
    class Meta:
        model = ActividadDeportiva
        fields = ['nombre', 'descripcion', 'lugar', 'cupo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Fútbol Masculino'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción detallada'}),
            'lugar': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Cancha Principal'}),
            'cupo': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }