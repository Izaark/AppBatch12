from django.conf.urls import url,include
from django.contrib.auth.views import login,logout_then_login
from django.contrib import admin
import urls_api

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^usuario/', include("Usuario.urls",namespace='Usuarios')),
	url(r'^login/',login,{'template_name':'index.html'}, name='login'),
	url(r'^logout/',logout_then_login, name='logout'),
    url(r'^api/v1/', include(urls_api))
    
]
