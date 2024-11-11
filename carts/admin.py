# carts/admin.py
from django.contrib import admin
from .models import Cart, CartItem

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'cart', 'quantity', 'is_active')
    list_filter = ('product', 'cart', 'is_active')
    search_fields = ('product__product_name', 'cart__cart_id')
    filter_horizontal = ('variations',)  # Enable horizontal filter for variations

admin.site.register(Cart)
admin.site.register(CartItem, CartItemAdmin)
