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
            'Torax':'Torax',
            'Brazo_Derecho':'Brazo Derecho',
            'Brazo_Relajado':'Brazo Relajado',
            'Cadera':'Cadera',
            'Cintura':'Cintura',
            'Muslo_Derecho_Contraido':'Muslo Derecho Contraido',
            'Pantorrilla_Derecha_Contraida':'Pantorrilla Derecha Contraida',
            'Brazo_Izquierdo':'Brazo Izquierdo',
            'Muslo_Izquierdo_Contraido':'Muslo Izquierdo Contraido',
            'Pantorrilla_Izquierda_Contraida':'Pantorrilla Izquierda Contraida',
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