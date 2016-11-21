from rest_framework import serializers
from .models import Direccion,Colonia
from Usuario.serializers import UsuarioSerializer

class DireccionSerializer(serializers.ModelSerializer):
	direccion_usuario = UsuarioSerializer(many = True, read_only= True)	
	class Meta:
		model = Direccion
		fields = ['id','slug','calle','numero_interior','numero_exterior','direccion_usuario']

class ColoniaSerializer(serializers.ModelSerializer):	
	class Meta:
		model = Colonia
		fields = ['nombre']