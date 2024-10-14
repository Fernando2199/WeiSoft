from django.contrib import admin
from .models import Notification, Driver

# Registrar los modelos para que sean accesibles desde el admin
admin.site.register(Notification)
admin.site.register(Driver)