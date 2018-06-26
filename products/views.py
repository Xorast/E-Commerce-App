from django.shortcuts   import render, get_object_or_404
from .models            import Product
from django.http        import HttpResponse

def get_products(request):
    products = Product.objects.all()
    return render(request, "products/products.html", {'products': products})


def cart_item_added(request):
    id = request.POST["product_id"]
    product = get_object_or_404(Product, pk=id)
    return HttpResponse("Item added to cart :" + Product.name)
    
