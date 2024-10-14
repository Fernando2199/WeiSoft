from django.contrib import admin
from django.urls import path, include
from notifications.views import home

urlpatterns = [
    path('', home, name='home'),  # Vista para la URL raíz
    path('admin/', admin.site.urls),  # URL para la página de administración
    path('notifications/', include('notifications.urls')),  # Incluir URLs de la aplicación de notificaciones
]