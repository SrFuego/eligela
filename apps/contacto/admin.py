# Python imports


# Django imports
from django.contrib import admin


# Local imports
from .models import Colegio


# Register your models here.
@admin.register(Colegio)
class ColegioAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'distrito',
        'telefono',
        'direccion',
    )
    search_fields = ('nombre',)
    ordering = ('nombre',)
