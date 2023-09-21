from django import forms
from apps.medidas.models import medidas

class medidasform(forms.ModelForm):
    class Meta:
        model=medidas    
        fields = [
            'Torax',
            'Brazo_Derecho',
            'Brazo_Relajado',
            'Cadera',
            'Cintura',
            'Muslo_Derecho_Contraido',
            'Pantorrilla_Derecha_Contraida',
            'Brazo_Izquierdo',
            'Muslo_Izquierdo_Contraido',
            'Pantorrilla_Izquierda_Contraida',
        ]
        labels= {
            'Torax':'Torax (cm)',
            'Brazo_Derecho':'Brazo Derecho (cm)',
            'Brazo_Relajado':'Brazo Relajado (cm)',
            'Cadera':'Cadera (cm)',
            'Cintura':'Cintura (cm)',
            'Muslo_Derecho_Contraido':'Muslo Derecho Contraido (cm)',
            'Pantorrilla_Derecha_Contraida':'Pantorrilla Derecha Contraida (cm)',
            'Brazo_Izquierdo':'Brazo Izquierdo (cm)',
            'Muslo_Izquierdo_Contraido':'Muslo Izquierdo Contraido (cm)',
            'Pantorrilla_Izquierda_Contraida':'Pantorrilla Izquierda Contraida (cm)',
        }
        widgets = {
            'Torax': forms.NumberInput(attrs={'class': 'form-control'}),
            'Brazo_Derecho': forms.NumberInput(attrs={'class': 'form-control'}),
            'Brazo_Relajado': forms.NumberInput(attrs={'class': 'form-control'}),
            'Cadera': forms.NumberInput(attrs={'class': 'form-control'}),
            'Cintura': forms.NumberInput(attrs={'class': 'form-control'}),
            'Muslo_Derecho_Contraido': forms.NumberInput(attrs={'class': 'form-control'}),
            'Pantorrilla_Derecha_Contraida': forms.NumberInput(attrs={'class': 'form-control'}),
            'Brazo_Izquierdo': forms.NumberInput(attrs={'class': 'form-control'}),
            'Muslo_Izquierdo_Contraido': forms.NumberInput(attrs={'class': 'form-control'}),
            'Pantorrilla_Izquierda_Contraida': forms.NumberInput(attrs={'class': 'form-control'}),
        }