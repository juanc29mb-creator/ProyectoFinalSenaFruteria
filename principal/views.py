from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from .models import Producto, Categoria


def inicio(request):
    """
    Vista principal de la tienda (Diseño de Guti: Mercado Campesino).
    Renderiza los productos y categorías directamente desde la base de datos con el ORM.
    """
    productos = Producto.objects.select_related('categoria').all().order_by('id_producto')
    categorias = Categoria.objects.all()
    context = {
        'titulo': 'El Paso Frutería — Mercado Campesino',
        'productos': productos,
        'categorias': categorias,
        'total_productos': productos.count(),
    }
    return render(request, 'principal/index.html', context)


def tienda_view(request):
    """Vista de tienda alternativa del proyecto formativo."""
    productos = Producto.objects.select_related('categoria').all().order_by('id_producto')
    categorias = Categoria.objects.all()
    context = {
        'titulo': 'El Paso Frutería — Tienda Oficial',
        'productos': productos,
        'categorias': categorias,
        'total_productos': productos.count(),
    }
    return render(request, 'fruteria/tienda.html', context)


def catalogo_frutas_view(request):
    """
    Vista del catálogo especializado de frutas de El Paso Frutería con filtrado reactivo.
    """
    productos = Producto.objects.select_related('categoria').all().order_by('id_producto')
    categorias = Categoria.objects.all()
    context = {
        'titulo': 'Catálogo de Frutas Frescas — El Paso Frutería',
        'productos': productos,
        'categorias': categorias,
        'total_productos': productos.count(),
    }
    return render(request, 'fruteria/catalogo_frutas.html', context)


@login_required
def dashboard_view(request):
    """
    Panel administrativo estilizado (Dashboard de Guti con métricas en tiempo real).
    """
    from django.contrib.auth import get_user_model
    User = get_user_model()
    productos = Producto.objects.select_related('categoria').all().order_by('id_producto')
    categorias = Categoria.objects.all()
    total_productos = productos.count()
    total_usuarios = User.objects.count()
    return render(request, 'principal/dashboard.html', {
        'productos': productos,
        'categorias': categorias,
        'total_productos': total_productos,
        'total_usuarios': total_usuarios,
    })


def logout_view(request):
    logout(request)
    return redirect('index')


def admin_preview(request):
    """Vista de previsualización autenticada para capturas del informe técnico."""
    from django.contrib import admin
    from django.contrib.auth.models import User
    user = User.objects.filter(username='admin').first()
    if user:
        request.user = user
    return admin.site.index(request)


def admin_productos_preview(request):
    """Vista de previsualización de la app principal en el panel de administración."""
    from django.contrib import admin
    from django.contrib.auth.models import User
    user = User.objects.filter(username='admin').first()
    if user:
        request.user = user
    return admin.site.app_index(request, 'principal')


def admin_producto_list_preview(request):
    """Vista de previsualización de la lista de productos en el panel de administración."""
    from django.contrib import admin
    from django.contrib.auth.models import User
    user = User.objects.filter(username='admin').first()
    if user:
        request.user = user
    from .models import Producto
    return admin.site._registry[Producto].changelist_view(request)