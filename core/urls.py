from django.contrib import admin
from django.urls import path, include

from plataforma.routing import websocket_urlpatterns

urlpatterns = [
    path('', include('plataforma.urls')),
    path('admin/', admin.site.urls),
    path('ws/', include(websocket_urlpatterns)),

]