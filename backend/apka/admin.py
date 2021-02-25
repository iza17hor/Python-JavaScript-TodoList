from django.contrib import admin

from .models import Dni, Cele

admin.site.register(Dni)
admin.site.register(Cele)


#Rejestrowanie modeli aby były widoczne w panelu admin.