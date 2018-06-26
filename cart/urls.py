from django.urls    import path
from .views         import display_content, cart_item_added


urlpatterns = [
    path('view',    display_content,    name='display_content'),
    path('item_added', cart_item_added,   name='cart_item_added'),
]
