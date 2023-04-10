from django.contrib import admin
from .models import Empresas, Suc_Empresa, Representante

# Register your models here.

class AdminEmpresas(admin.ModelAdmin):
    list_display = ('nombre', 'created_at', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('nombre', 'id')
admin.site.register(Empresas, AdminEmpresas)

class AdminSuc(admin.ModelAdmin):
    list_display = ('nombre', 'created_at', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('nombre', 'id')
admin.site.register(Suc_Empresa, AdminSuc)

class AdminRepresentate(admin.ModelAdmin):
    list_display = ('nombre', 'created_at', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('nombre', 'id')
admin.site.register(Representante, AdminRepresentate)
