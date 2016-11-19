from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from .views_apiset import UsuarioViewSet

router = DefaultRouter()
router.register(r'',UsuarioViewSet)

urlpatterns = [
	url(r'^listado_api_user/', include(router.urls)),
]