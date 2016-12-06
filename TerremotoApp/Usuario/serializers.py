from rest_framework import serializers
from .models import Usuario,Interes



class InteresesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Interes
		fields = ['nombre','es_exterior']

class AmigosSerializer(serializers.ModelSerializer):
	class Meta:
		model = Usuario
		fields = ['first_name','last_name']

class UsuarioSerializer(serializers.ModelSerializer):
	intereses_usuario = InteresesSerializer(source="intereses" ,many=True,read_only=True)
	amigos_usuario = AmigosSerializer(source="circulo_amigos", many=True, read_only=True)
	class Meta:
		model = Usuario
		fields = ['id','username','first_name','last_name','email','is_active','direccion','telefono','intereses_usuario','amigos_usuario']



