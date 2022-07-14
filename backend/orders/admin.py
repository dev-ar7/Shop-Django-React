from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):

    list_display = ('id', 'full_name', 'phone_num', 
                    'full_address', 'status', 
                    'created_at', 'updated_at')


admin.site.register(Order, OrderAdmin)
