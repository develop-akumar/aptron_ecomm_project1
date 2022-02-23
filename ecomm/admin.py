from django.contrib import admin
from .models import order, product, register_info, category                 

# Register your models here.

admin.site.register(register_info)
admin.site.register(product)
admin.site.register(category)
admin.site.register(order)
