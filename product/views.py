from django.shortcuts import render
from .models import Product,Category,Brand,ProductImage
# Create your views here.

def product_list(request):
    productslist=Product.objects.all()
    categories=Category.objects.all()
    context={
        'categories':categories,
        'productslist':productslist
    }
    if request.GET.get('category'):
        productslist=productslist.filter(category__category_name=request.GET.get('category'))
        context={
            'categories':categories,
            'productslist':productslist
        }
    return render(request,'product_list.html',context)
def product_detail(request,id):
    product=Product.objects.get(id=id)
    images=ProductImage.objects.filter(product=product)
    context={
        'product':product,
        'images':images
    }
    return render(request,'product_detail.html',context)

    