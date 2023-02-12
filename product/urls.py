

from django.urls import path
from product import views #app view 

app_name='product'

urlpatterns = [
    
    path('',views.product_list,name='productlist'),
    path('<int:id>',views.product_detail,name='productdetail'),
]
