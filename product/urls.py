

from django.urls import path
from product import views #app view 

app_name='product'

urlpatterns = [
    
    path('',views.product_list,name='productlist'),
    
    path('<int:id>',views.product_detail,name='productdetail'),

    path('productslist',views.product_list_api.as_view()),
    path('categorieslist',views.categories_list_api.as_view()),
    path('brandslist',views.brands_list_api.as_view()),

]
