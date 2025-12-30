import os
import django
from django.core.asgi import get_asgi_application 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

# Importe seus módulos após a configuração do Django
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
import plataforma.routing


django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                plataforma.routing.websocket_urlpatterns  # Inclua suas rotas WebSocket aqui
            )
        )
    ),
})