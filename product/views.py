from django.shortcuts import render
from .models import Product,Category,Brand,ProductImage
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status,generics
from product.serializers import ProductSerializer,CategorySerializer,BrandSerializer
from rest_framework import filters

@api_view(['GET','POST'])


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


class product_list_api(generics.ListCreateAPIView):
    
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class categories_list_api(generics.ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

class brands_list_api(generics.ListCreateAPIView):
    queryset=Brand.objects.all()
    serializer_class=BrandSerializer        

