from django.conf.urls import url
from .views import UsuarioListView

urlpatterns = [
url(r'^lista/$', UsuarioListView.as_view(), name='listado_usuarios'),

]