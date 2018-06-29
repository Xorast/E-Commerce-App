from django.shortcuts   import render, get_object_or_404, redirect
from django.http        import HttpResponse
from products.models    import Product
from .utils             import get_cart_items_and_total
# Here is the difference : Using forms.



def display_content(request):
    cart          = request.session.get("cart", {})
    context       = get_cart_items_and_total(cart)
    
    return render(request, 'cart/cart-view.html', context)
    
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
    return redirect("get_products")
    
    
def cart_item_removed(request):
    
    id          = request.POST.get("product_id")
    cart        = request.session.get("cart", {})
    cart.pop(id, None)
    
    # cart[id]    = 0
   
    request.session['cart'] = cart
    
    # Redirect somewhere
    return redirect("/cart/view")