from django.shortcuts   import render, get_object_or_404
from django.http        import HttpResponse
from products.models    import Product
# Here is the difference : Using forms.



def display_content(request):
    cart        = request.session.get("cart", {})
    
    # Lists of the products in the cart
    products    = []
    overall_total = 0

    for key in cart:
        item        = get_object_or_404(Product, pk=key)
        cart_item   = { "product"   : item, 
                        "quantity"  : cart[key], 
                        "sub_total"     : item.price * cart[key]  }
        products.append(cart_item)
        # overall_total += item.price * cart[key]
        overall_total += cart_item["sub_total"]
    
    return render(request, 'cart/cart-view.html', {"products" : products, "overall_total" : overall_total})
    
def cart_item_added(request):
    
    id          = request.POST["product_id"]
    product     = get_object_or_404(Product, pk=id)
    
    # Get the current Cart
    cart        = request.session.get('cart', {})
    
    # Update the Cart
    cart[id]    = cart.get(id,0) + 1
    
    # Save the Cart back to the session
    request.session['cart'] = cart
    
    # Redirect somewhere
    return HttpResponse(cart[id])