from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .serializers import ColoniaSerializer
from .models import Colonia

class ColoniaListadoview(APIView):
	'''Devuelve listado de Senseis'''
	def get(self, request, format=None):
		listado = Colonia.objects.all()
		serializer = ColoniaSerializer(listado, many=True)
		return Response(serializer.data)

class ColoniaDetail(generics.RetrieveUpdateDestroyAPIView):
	
	queryset = Colonia.objects.all()
	serializer_class = ColoniaSerializer