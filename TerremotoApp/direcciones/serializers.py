from rest_framework import serializers
from .models import Colonia

class ColoniaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Colonia
		fields = ["codigo_postal", "nombre", "municipio", "ciudad","estado","pais"]