from django.shortcuts   import render, get_object_or_404
from django.http        import HttpResponse
from products.models    import Product
# Here is the difference : Using forms.



def display_content(request):
    return render(request, 'cart/cart-view.html')
    
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