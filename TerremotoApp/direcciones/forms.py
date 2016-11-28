from django import forms
from .models import Direccion

class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = [
        	'slug',
        	'calle',
        	'numero_exterior',
        	'numero_interior',
    	]
        labels = {
        'slug':"calle",
        'calle':"Calle y numero",
        'numero_exterior':"Numero exterior",
        'numero_interior':"Numero interior",
  	
    	}
        widgets={
        'slug':forms.TextInput(attrs={'class':'form-control'}),
        'calle':forms.TextInput(attrs={'class':'form-control'}),
        'numero_exterior':forms.TextInput(attrs={'class':'form-control'}),
        'numero_interior':forms.TextInput(attrs={'class':'form-control'}),
    	}