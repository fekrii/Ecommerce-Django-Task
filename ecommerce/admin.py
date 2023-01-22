from django.contrib import admin
from .models import Item, OrderItem, Order




class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'description', 'image']


admin.site.register(Item, ItemAdmin)
admin.site.register(OrderItem)
admin.site.register(Order)
