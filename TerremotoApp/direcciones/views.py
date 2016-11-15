from django.shortcuts import render
from sensei.serializers import ColoniaSerializer
from sensei.models import Colonia
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
class ColoniaList(APIView):
	def get(self, request, format=None):
		coloniaser= Colonia.objects.all()
		serializer = ColoniaSerializer(coloniaser, many=True)
		return Response(serializer.data)