from .models import Cart, CartItem
from .views import _cart_id

def counter(request):
    cart_count = 0
    if 'admin' in request.path:
        return {}
    
    try:
        # Get the cart for the current session
        cart = Cart.objects.get(cart_id=_cart_id(request))
        
        # Filter cart items based on the retrieved cart
        cart_items = CartItem.objects.filter(cart=cart)
        
        # Count the total quantity of items in the cart
        for cart_item in cart_items:
            cart_count += cart_item.quantity
            
    except Cart.DoesNotExist:
        cart_count = 0

    return dict(cart_count=cart_count)
