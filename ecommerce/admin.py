from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(TipoMovimiento)
admin.site.register(Moneda)
admin.site.register(Impuestos)
admin.site.register(Producto)
admin.site.register(ProductoImpuesto)
admin.site.register(CuponDescuento)
admin.site.register(Concepto)
admin.site.register(EstadosEcommerce)