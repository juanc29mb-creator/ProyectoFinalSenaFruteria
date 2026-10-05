from django.contrib import admin
from django.urls import path, include
from principal.views import (
    inicio,
    tienda_view,
    catalogo_frutas_view,
    dashboard_view,
    logout_view,
    admin_preview,
    admin_productos_preview,
    admin_producto_list_preview
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin-preview/', admin_preview, name='admin_preview'),
    path('admin-preview/principal/', admin_productos_preview, name='admin_productos_preview'),
    path('admin-preview/principal/producto/', admin_producto_list_preview, name='admin_producto_list_preview'),
    path('', inicio, name='index'),
    path('inicio/', inicio, name='inicio'),
    path('tienda/', tienda_view, name='tienda'),
    path('catalogo-frutas/', catalogo_frutas_view, name='catalogo_frutas'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='principal/login.html'), name='login'),
    path('accounts/logout/', logout_view, name='logout'),
]
