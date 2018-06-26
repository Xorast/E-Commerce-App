from django.urls    import path
from .views         import get_products, cart_item_added

urlpatterns = [
    path('', get_products,      name='get_products'),
    path('cart_item_added', cart_item_added,   name='cart_item_added'),
]
