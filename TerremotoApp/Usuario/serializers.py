from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Usuario
		fields = ['id','username','first_name','last_name','email','is_active','direccion','telefono','intereses','circulo_amigos']