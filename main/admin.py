from django.contrib import admin
from .models import *


@admin.register(Puesto, Trabajador, Producto)
class PonysAdmin(admin.ModelAdmin):
	pass
