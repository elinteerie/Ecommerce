from django.contrib import admin

from .models import Product
admin.site.site_header = "Ecommerce Site"
admin.site.site_title = "ABC Shopping"
admin.site.index_title = "Manage ABC Shopping"
# Register your models here.
admin.site.register(Product)
