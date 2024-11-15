from .models import Cart, CartItem
from .views import _cart_id

def counter(request):
    cart_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            # Get the cart as a queryset to apply slicing
            cart = Cart.objects.filter(cart_id=_cart_id(request))[:1]
            if request.user.is_authenticated:
                cart_items = CartItem.objects.filter(user=request.user)
            else:
                cart_items = CartItem.objects.filter(cart__in=cart)  # Using __in to filter with a queryset
            
            # Count the total quantity of items in the cart
            for cart_item in cart_items:
                cart_count += cart_item.quantity
                
        except Cart.DoesNotExist:
            cart_count = 0

    return dict(cart_count=cart_count)
