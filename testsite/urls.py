from django.contrib import admin
from django.urls import path,include
from django.conf import settings
admin.site.site_title="Buy/Sell Admin Portal"
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',include('userAuth.app_urls')),
    path('',include('djApp.app_urls')),
    path('products/',include('product.urls',namespace='product')),
    path('', include('chat.urls', namespace='chat')),

]
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



