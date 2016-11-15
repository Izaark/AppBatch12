from django.conf.urls import url
from .views_api import ColoniaListadoview

urlpatterns = [
	url(r'^api/v1/', include(urls_api))
]