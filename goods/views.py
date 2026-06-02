from django.shortcuts import render
from goods.models import Product

def catalog(request):
    goods=Product.objects.all()

    context={
        'title':'Home - Catalog',
        'goods': goods,

    }
    return render(request, 'goods/catalog.html',context)

def product(request,product_id):
    product=Product.objects.get(id=product_id)
    context={'product':product,}
    return render(request, 'goods/product.html',context)