from django.shortcuts import render
from .serializers import ColoniaSerializer
from django.views.generic  import ListView, CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Colonia,Direccion
from .forms import DireccionForm
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
class ColoniaList(APIView):
	def get(self, request, format=None):
		coloniaser= Colonia.objects.all()
		serializer = ColoniaSerializer(coloniaser, many=True)
		return Response(serializer.data)


class DireccionListView(ListView):
    model = Direccion
    template_name = "direccion_list.html"
    paginate_by = 2

class DireccionCreateView(CreateView):
	model = Direccion
	form_class = DireccionForm
	template_name = 'direccion_forms.html'
	success_url = reverse_lazy('direcciones:direccion_listar')

class DireccionUpdateView(UpdateView):
	model = Direccion
	form_class = DireccionForm
	template_name = 'direccion_forms.html'
	success_url = reverse_lazy('direcciones:direccion_listar')


class DireccionDeleteView(DeleteView):
	model = Direccion
	template_name = 'direccion_delete.html'
	success_url = reverse_lazy('direcciones:direccion_listar')