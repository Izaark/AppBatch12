from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from .views_apiset import UsuarioViewSet,UsuarioList,InteresesList
router = DefaultRouter()
router.register(r'',UsuarioViewSet)

urlpatterns = [
	url(r'^listado_api_user/', include(router.urls)),
	url(r'^listado_api_user_filter/', UsuarioList.as_view()),
	url(r'^intereses/',InteresesList.as_view()),
]