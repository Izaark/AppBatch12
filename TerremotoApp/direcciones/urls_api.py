from django.conf.urls import url,include
from .views_api import ColoniaListadoview
from rest_framework.routers import DefaultRouter
from .views_apiset import ColoniaViewSet

router = DefaultRouter()
router.register(r'',ColoniaViewSet)

urlpatterns = [
	url(r'^listado/', ColoniaListadoview.as_view()),
	url(r'^listado_api/', include(router.urls)),
]