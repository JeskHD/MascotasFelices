from django.contrib import admin
from .models import Cliente, Mascota, HistorialMedico

class MascotaInline(admin.TabularInline):
    model = Mascota
    extra = 0

class ClienteAdmin(admin.ModelAdmin):
    inlines = [MascotaInline]
    list_display = ('nombre', 'telefono', 'email')
    search_fields = ('nombre', 'telefono', 'email')

class HistorialMedicoInline(admin.TabularInline):
    model = HistorialMedico
    extra = 0

class MascotaAdmin(admin.ModelAdmin):
    inlines = [HistorialMedicoInline]
    list_display = ('nombre', 'especie', 'raza', 'edad', 'cliente')
    search_fields = ('nombre', 'especie', 'raza', 'cliente__nombre')

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Mascota, MascotaAdmin)
