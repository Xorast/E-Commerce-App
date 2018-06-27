from django.urls    import path
from .views         import display_content, cart_item_added, cart_item_removed


urlpatterns = [
    path('view',    display_content,    name='display_content'),
    path('item_added', cart_item_added,   name='cart_item_added'),
    path('item_removed', cart_item_removed,   name='cart_item_removed'),
]
