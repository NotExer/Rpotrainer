from django import forms
from apps.diagnostico.models import diagnostico

class diagnosticoform(forms.ModelForm):
    class Meta:
        model=diagnostico
        
        fields = [
            'Edad',
            'Telefono',
            'Email',
            'Domicilio',
            'Objetivo_Fisico',
            'Nivel_entrenamiento_años',
            'Frecuencia_semanal',
            'Dias_de_entrenamiento',
            'Tiempo_Por_Sesion',
            'Material_Entreno',
            'Fuma',
            'Consume_alcohol',
            'Cirugias_anteriores',
            'Enfermedad_de_base',
            'Entrenos_anteriores',
            'Fracturas',
            'Tiempo_sueño',
        ]
        
        labels= {
            'Edad': 'Edad',
            'Telefono':'Teléfono',
            'Email':'Email',
            'Domicilio': 'Domicilio',
            'Objetivo_Fisico':'Objetivo Físico',
            'Nivel_entrenamiento_años':'Nivel de entrenamiento (años)',
            'Frecuencia_semanal':'Frecuencia semanal',
            'Dias_de_entrenamiento':'Días de entrenamiento',
            'Tiempo_Por_Sesion':'Tiempo por sesión',
            'Material_Entreno':'Material de entreno',
            'Fuma':'¿Fuma?',
            'Consume_alcohol':'¿Consume alcohol?',
            'Cirugias_anteriores':'Cirugías anteriores',
            'Enfermedad_de_base':'Enfermedad de base',
            'Entrenos_anteriores':'Entrenos anteriores',
            'Fracturas': 'Fracturas',
            'Tiempo_sueño':'Tiempo sueño',
        }
        widgets = {
            'Edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'Telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control'}),
            'Domicilio': forms.Textarea(attrs={'class': 'form-contrl'}),
            'Objetivo_Fisico': forms.TextInput(attrs={'class': 'form-control'}),
            'Nivel_entrenamiento_años': forms.NumberInput(attrs={'class': 'form-control'}),
            'Frecuencia_semanal': forms.NumberInput(attrs={'class': 'form-control'}),
            'Dias_de_entrenamiento': forms.NumberInput(attrs={'class': 'form-control'}),
            'Tiempo_Por_Sesion': forms.NumberInput(attrs={'class': 'form-control'}),
            'Material_Entreno': forms.TextInput(attrs={'class': 'form-control'}),
            'Fuma': forms.TextInput(attrs={'class': 'form-control'}),
            'Consume_alcohol': forms.TextInput(attrs={'class': 'form-control'}),
            'Cirugias_anteriores': forms.TextInput(attrs={'class': 'form-control'}),
            'Entrenos_anteriores': forms.TextInput(attrs={'class': 'form-control'}),
            'Enfermedad_de_base': forms.TextInput(attrs={'class': 'form-control'}),
            'Fracturas': forms.TextInput(attrs={'class': 'form-control'}),
            'Tiempo_sueño': forms.NumberInput(attrs={'class': 'form-control'}),
        }