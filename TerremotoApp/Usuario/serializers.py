from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Usuario
		fields = ["id","username","first_name","email","_direccion","telefono","profesion","circulo_amigos"]