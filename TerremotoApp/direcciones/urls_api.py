from django.conf.urls import url
from .views_api import ColoniaListadoview

urlpatterns = [
	url(r'^listado/', ColoniaListadoview.as_view()),
]