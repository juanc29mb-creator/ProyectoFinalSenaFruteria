from django.db import models


class Categoria(models.Model):
    id_categoria = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=60, verbose_name="Nombre de Categoría")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        db_table = "categorias"

    def __str__(self):
        return self.nombre


class Proveedor(models.Model):
    id_proveedor = models.BigAutoField(primary_key=True)
    razon_social = models.CharField(max_length=150, verbose_name="Razón Social")
    nit_rut = models.CharField(max_length=30, unique=True, verbose_name="NIT / RUT")
    contacto_nombre = models.CharField(max_length=100, blank=True, null=True, verbose_name="Nombre de Contacto")
    telefono = models.CharField(max_length=20, blank=True, null=True, verbose_name="Teléfono")
    email = models.EmailField(max_length=100, blank=True, null=True, verbose_name="Correo Electrónico")
    calificacion_estrellas = models.DecimalField(
        max_digits=2, decimal_places=1, default=5.0, verbose_name="Calificación (Estrellas)"
    )
    estado = models.CharField(max_length=20, default="Activo", verbose_name="Estado")

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        db_table = "proveedores"

    def __str__(self):
        return f"{self.razon_social} ({self.nit_rut})"


class Producto(models.Model):
    ESTADO_CHOICES = [
        ("Disponible", "Disponible"),
        ("Agotado", "Agotado"),
        ("En Maduracion", "En Maduración"),
    ]

    id_producto = models.BigAutoField(primary_key=True)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name="productos",
        verbose_name="Categoría"
    )
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Producto")
    icono_emoji = models.CharField(max_length=10, default="🍎", verbose_name="Icono / Emoji")
    imagen_url = models.URLField(max_length=500, blank=True, null=True, verbose_name="URL de Imagen")
    origen = models.CharField(max_length=150, default="🌱 Cosecha: Hace 1 día • Finca El Campo", verbose_name="Origen / Cosecha")
    unidad_medida = models.CharField(max_length=20, default="kg", verbose_name="Unidad de Medida")
    brix_minimo = models.DecimalField(
        max_digits=4, decimal_places=2, default=0.00, verbose_name="°Brix Mínimo (Dulzor)"
    )
    stock_actual = models.DecimalField(
        max_digits=10, decimal_places=3, default=0.000, verbose_name="Stock Actual"
    )
    stock_minimo = models.DecimalField(
        max_digits=10, decimal_places=3, default=0.000, verbose_name="Stock Mínimo"
    )
    precio_venta_unitario = models.DecimalField(
        max_digits=12, decimal_places=2, verbose_name="Precio de Venta Unitario"
    )
    estado = models.CharField(
        max_length=20, choices=ESTADO_CHOICES, default="Disponible", verbose_name="Estado"
    )

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        db_table = "productos"

    @property
    def precio(self):
        """Compatibilidad con plantillas que usan producto.precio"""
        return self.precio_venta_unitario

    @property
    def stock(self):
        """Compatibilidad con plantillas que usan producto.stock"""
        return int(self.stock_actual)

    def __str__(self):
        return f"{self.icono_emoji} {self.nombre} - ${self.precio_venta_unitario:,.0f} / {self.unidad_medida}"


class Cliente(models.Model):
    TIPO_CHOICES = [
        ("DETAL", "Al Detal"),
        ("MAYORISTA", "Mayorista"),
    ]

    id_cliente = models.BigAutoField(primary_key=True)
    tipo_cliente = models.CharField(max_length=10, choices=TIPO_CHOICES, default="DETAL", verbose_name="Tipo de Cliente")
    cupo_credito = models.DecimalField(max_digits=12, decimal_places=2, default=0.00, verbose_name="Cupo de Crédito")
    puntos_fidelidad = models.IntegerField(default=0, verbose_name="Puntos de Fidelidad")

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        db_table = "clientes"

    def __str__(self):
        return f"Cliente #{self.id_cliente} ({self.tipo_cliente})"
