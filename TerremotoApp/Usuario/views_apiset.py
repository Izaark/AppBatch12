from rest_framework import filters
from rest_framework import generics
from rest_framework import viewsets
from .serializers import UsuarioSerializer
from .models import Usuario

class UsuarioViewSet(viewsets.ModelViewSet):
	queryset = Usuario.objects.all()
	serializer_class = UsuarioSerializer

class UsuarioList(generics.ListCreateAPIView):
	queryset = Usuario.objects.all()
	serializer_class = UsuarioSerializer
	filter_backends = (filters.SearchFilter, filters.DjangoFilterBackend,)
	filter_fields = ('is_active',)
	search_fields = ('username','first_name','last_name','email',)