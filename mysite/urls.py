from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static 
from django.conf import settings 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('user/', include('users.urls')),
    path('business/', include('business.urls')),
    path('customer/', include('customer.urls')),
    path('orders/', include('orders.urls')),
    path('delivery/', include('delivery.urls'))
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

