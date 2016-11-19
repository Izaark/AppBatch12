from rest_framework import serializers
from .models import Direccion,Colonia
from Usuario.serializers import UsuarioSerializer

class DireccionSerializer(serializers.ModelSerializer):
	usuario = UsuarioSerializer(many = True, read_only= True)	
	class Meta:
		model = Direccion
		fields = ['id','slug','calle','usuario']

class ColoniaSerializer(serializers.ModelSerializer):	
	class Meta:
		model = Colonia
		fields = ['nombre']