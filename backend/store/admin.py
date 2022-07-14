from django.contrib import admin
from .models import Product, Rating


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'inventory', 'updated_at')
    prepopulated_fields = {"slug": ("name",)}

class RatingAdmin(admin.ModelAdmin):
    list_display = ('product', 'one', 'two', 'three', 'four', 'five')


admin.site.register(Product)
admin.site.register(Rating)
