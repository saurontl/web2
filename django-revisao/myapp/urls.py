from django.urls import path
from .views import get_clients
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('clients/', get_clients, name='get_clients'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


