from rest_framework import viewsets
from .models import Colonia
from .serializers import ColoniaSerializer

class ColoniaViewSet(viewsets.ModelViewSet):
	queryset = Colonia.objects.all()
	serializer_class = ColoniaSerializer