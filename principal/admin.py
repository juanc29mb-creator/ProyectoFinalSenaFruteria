from django.contrib import admin
from .models import Categoria, Proveedor, Producto, Cliente


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id_categoria', 'nombre', 'descripcion')
    search_fields = ('nombre',)


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id_proveedor', 'razon_social', 'nit_rut', 'contacto_nombre', 'telefono', 'calificacion_estrellas', 'estado')
    search_fields = ('razon_social', 'nit_rut', 'contacto_nombre')
    list_filter = ('estado',)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id_producto', 'icono_emoji', 'nombre', 'categoria', 'precio_venta_unitario', 'stock_actual', 'unidad_medida', 'brix_minimo', 'estado')
    search_fields = ('nombre', 'categoria__nombre', 'origen')
    list_filter = ('categoria', 'estado', 'unidad_medida')
    list_editable = ('precio_venta_unitario', 'stock_actual', 'estado')


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id_cliente', 'tipo_cliente', 'cupo_credito', 'puntos_fidelidad')
    list_filter = ('tipo_cliente',)
