from django.conf.urls import url,include
from .views import get_api_weather

urlpatterns = [
	url(r'^weather/', get_api_weather, name='clima'),
]